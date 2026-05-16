
## PPO‑EAM‑DRL: Deep Reinforcement Learning for Global Minimum Search in Bimetallic Nanoclusters with Generalization to Transition Metals
Proximal policy optimization combined with embedded atom method potentials for efficient global minimum search across transition metals
## How to Run the Code

1. **Set Up the Environment:**
   - Install the required Conda environment using the provided YAML file:
     ```bash
     conda env create -f env_Deepcluster.yml
     ```
2. **Activate the Environment:**
   - Activate the `Deepcluster` environment by using the following command:
     ```bash
     conda activate Deepcluster
     ```
4. **Configure the Nanocluster Composition:**
   - Edit `gym_ppo_single.py` for PPO with EAM Potential to select the nanocluster composition.
     
5. **Run the Simulation:**
   - Execute the script using Python.
     ```bash
     python gym_ppo_single.py
