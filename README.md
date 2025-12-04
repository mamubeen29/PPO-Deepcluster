# Deepcluster Agent Agent For Efficient Discovery of Global Minima Structures in Ag–Cu Nanoalloys by Deep Reinforcement Learning
## How to Run the Code

1. **Set Up the Environment:**
   - Install the required Conda environment using the provided YAML file:
     ```bash
     conda env create -f Deepcluster.yml
     ```
2. **Activate the Environment:**
     ```bash
     conda activate Deepcluster
     ```
3. **Configure the Nanocluster Composition:**
   - Edit Deepcluster.py to select the nanocluster composition.
     
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
4. **Run the Simulation:**
   - Execute the script using Python.
     ```bash
     python Deepcluster.py  
