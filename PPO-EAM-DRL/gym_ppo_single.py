import matplotlib
matplotlib.use("Agg")

# ---------------------------------------------------------------------------
# GPU Acceleration Configuration
# Must be done BEFORE importing TensorFlow or TensorForce.
# ---------------------------------------------------------------------------
import tensorflow as tf

def configure_gpu():
    """
    Configure TensorFlow GPU settings:
      1. Set inter/intra-op parallelism threads (must be done FIRST).
      2. Enable memory growth so TF does not grab all VRAM at once.
      3. Print a summary of visible devices.
    """
    # IMPORTANT: Thread settings must be set before any other TF calls.
    tf.config.threading.set_inter_op_parallelism_threads(4)
    tf.config.threading.set_intra_op_parallelism_threads(4)

    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        try:
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)
            # Optionally restrict to a single GPU (comment out to use all GPUs):
            # tf.config.set_visible_devices(gpus[0], 'GPU')
            logical_gpus = tf.config.list_logical_devices('GPU')
            print(f"[GPU] {len(gpus)} Physical GPU(s) → {len(logical_gpus)} Logical GPU(s) configured.")
        except RuntimeError as e:
            # Memory growth must be set before GPUs are initialised.
            print(f"[GPU] RuntimeError during GPU configuration: {e}")
    else:
        print("[GPU] No GPU detected — running on CPU.")

    # Optional: limit TF log noise (0=all, 1=no INFO, 2=no WARNING, 3=no ERROR)
    import os
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

configure_gpu()

# ---------------------------------------------------------------------------
# Standard imports
# ---------------------------------------------------------------------------
import gym
from clusgym import MCSEnv
import gym.wrappers
import numpy as np
import tensorforce
from tensorforce.agents import Agent
from tensorforce.execution import Runner
import os
import copy
from callback import Callback

# ---------------------------------------------------------------------------
# Compatibility fix: tensorforce 0.5.5 + TensorFlow 2.12
#
# TF 2.12 resets Module class-level variables to None. Restore only the ones
# that need a non-None value; leave the rest as None (their correct default).
# ---------------------------------------------------------------------------
from tensorforce.core.module import Module

Module.global_scope        = ''   # str  – root TF name scope
Module.scope_stack         = []   # list – push/pop during graph build
Module.while_counter       = 0    # int  – compared with > 0
Module.cond_counter        = 0    # int  – compared with > 0
Module.global_tensors_spec = {}   # dict – keyed tensor specs
Module.global_tensors      = {}   # dict – keyed tensor objects
Module.queryable_tensors   = {}   # dict – item assignment used
# global_summary_step, set_parent, inherit_* stay None — correct defaults

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
timesteps = 200

# ── Composition ─────────────────────────────────────────────────────────────
# Monometallic # Bimetallic   # Trimetallic  
# Any combination supported by the Zhou-2004 EAM potential is valid.
# ────────────────────────────────────────────────────────────────────────────
eleNames  = ['Pt','Co']
eleNums   = [6,7]
clus_seed = None
save_dir  = 'result_' + ''.join(f"{name}{num}" for name, num in zip(eleNames, eleNums)) + '/'


def setup_env(recording=False):
    MCS_gym = MCSEnv(
        eleNames=eleNames,
        eleNums=eleNums,
        clus_seed=clus_seed,
        observation_fingerprints=True,
        save_dir=save_dir,
        timesteps=timesteps,
        save_every=1,
        n_unique_pool=25,
    )
    env = tensorforce.environments.OpenAIGym(
        MCS_gym,
        max_episode_timesteps=400,
        visualize=False,
    )
    return env


# ---------------------------------------------------------------------------
# Build the PPO agent
# TensorForce uses tf.keras layers internally; once the GPU is configured
# above, all graph operations (policy forward passes, gradient updates) run
# on the GPU automatically.
# ---------------------------------------------------------------------------
agent = Agent.create(
    agent='ppo',
    environment=setup_env(),
    batch_size=64,
    max_episode_timesteps=400,
    learning_rate=3e-4,
    subsampling_fraction=0.25,
    optimization_steps=10,
    likelihood_ratio_clipping=0.2,
    entropy_regularization=0.01,
    discount=0.99,

    # ── Network architecture ──────────────────────────────────────────────
    # Larger networks benefit more from GPU. Adjust width/depth to taste.
    ####],

    # ── Mixed-precision (optional, ~2× speedup on Ampere+ GPUs) ──────────
    # Uncomment the three lines below to enable float16 compute:
    # config=dict(
    #     device='GPU',
    # ),
)

agent_spec = agent.spec
print(agent_spec)

# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------
callback = Callback(save_dir).episode_finish

runner = Runner(
    agent=agent,
    environment=setup_env(recording=False),
    max_episode_timesteps=timesteps,
)

runner.run(num_episodes=3000, callback=callback, callback_episode_frequency=1)
runner.close()
