# Deepcluster Agent For Efficient Discovery of Global Minima Structures in Ag–Cu Nanoalloys by Deep Reinforcement Learning
## Clusgm-DRL: A Proximal Policy Optimization (PPO) framework for global minimum (GM) search on nanocluster potential energy surfaces (PES)
The framework models cluster optimization as a sequential decision-making process. An agent iteratively perturbs atomic coordinates (state St), receives the resulting energy (reward Rt), and updates its policy to favor moves that lower potential energy. Initially developed with Trust Region Policy Optimization (TRPO) in [clusgym_drl](https://github.com/rajeshkochi444/clusgm_drl) J. Phys. Chem. A 2024, 128, 42, 9122–9134. We thank the authors for making the code available on github. The framework has been upgraded to PPO to overcome TRPO’s computational bottlenecks and improve sample efficiency. The PPO update employs a clipped surrogate objective to constrain policy updates, enabling stable training on high-dimensional PES landscapes across diverse cluster types.
## How to Run the Code

1. **Set Up the Environment:**
   - Install the required Conda environment using the provided YAML file:
     ```bash
     conda env create -f env_clusgym.yml
     ```
2. **Activate the Environment:**
   - Activate the `Deepcluster` environment by using the following command:
     ```bash
     conda activate clusgym
     ```
4. **Configure the Nanocluster Composition:**
   - Edit `gym_trpo_single.py` for TRPO to select the nanocluster composition.
   - Edit `gym_ppo_single.py` for PPO to select the nanocluster composition.
     
     For simulating a mono metallic nanocluster change 'eleNames' and 'eleNums':
     - Ag13 Nanocluster:
     ```bash
     eleNames = ['Ag']
     eleNums = [13]
     ```
     - Cu13 Nanocluster:
     ```bash
     eleNames = ['Cu']
     eleNums = [13]
     ```

     For simulating a bi metallic nanocluster change 'eleNames' and 'eleNums':
     
     - Ag12Cu1 Nanocluster:
     ```bash
     eleNames = ['Ag','Cu']
     eleNums = [12,1]
     ```
     - Ag11Cu2 Nanocluster:
     ```bash
     eleNames = ['Ag','Cu']
     eleNums = [11,2]
     ```
     - Ag10Cu3 Nanocluster:
     ```bash
     eleNames = ['Ag','Cu']
     eleNums = [10,3]
     ```
     - Ag9Cu4 Nanocluster:
     ```bash
     eleNames = ['Ag','Cu']
     eleNums = [9,4]
     ```
     - Ag8Cu5 Nanocluster:
     ```bash
     eleNames = ['Ag','Cu']
     eleNums = [8,5]
     ```
     - Ag7Cu6 Nanocluster:
     ```bash
     eleNames = ['Ag','Cu']
     eleNums = [7,6]
     ```
     - Ag6Cu7 Nanocluster:
     ```bash
     eleNames = ['Ag','Cu']
     eleNums = [6,7]
     ```
     - Ag5Cu8 Nanocluster:
     ```bash
     eleNames = ['Ag','Cu']
     eleNums = [5,8]
     ```
     - Ag4Cu9 Nanocluster:
     ```bash
     eleNames = ['Ag','Cu']
     eleNums = [4,9]
     ```
     - Ag3Cu10 Nanocluster:
     ```bash
     eleNames = ['Ag','Cu']
     eleNums = [3,10]
     ```
     - Ag2Cu11 Nanocluster:
     ```bash
     eleNames = ['Ag','Cu']
     eleNums = [2,11]
     ```
     - Ag1Cu12 Nanocluster:
     ```bash
     eleNames = ['Ag','Cu']
     eleNums = [1,12]
     ```
5. **Run the Simulation:**
   - Execute the script using Python for TRPO.
     ```bash
     python gym_ppo_single.py

   - Execute the script using Python for PPO.
     ```bash
     python gym_trpo_single.py  
