# Programming Assignment 2: Estimating Transformations

## Assignment Info
[Programming Assignment 2 Info](pa_2.pdf)

## Anaconda
If you want to use just Python and not Colab, I highly recommend installing Anaconda. Anaconda is a necessity for data science and you should learn how to use it because it will change your life.

[Anaconda Download](https://www.anaconda.com/products/individual)

[Anaconda Cheat Sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

## Clone GitHub Repo
```
# Clone
git clone https://github.com/sawyermade/cvfa21netid_pa-2.git

# Change directory name to your netid, example using my netid
# You can also use file explorer, right-click, and rename
mv cvfa21netid_pa-2 danielsawyer_pa-2

# Enter directory, again using my netid as an example
cd danielsawyer_pa-2
```

## How To Run: Python

### Anaconda Environment Setup
```
# Install Anaconda Environment
conda env create -f environment.yml
conda activate cvpj2
```

OR

### Pip Setup
```
# Install Modules Pip
pip3 install -r requirements.txt
```

### Run program
```
# Runs program
python3 main.py
```

## How To Run: Colab
1. Open est_trans.py in a text editor and then copy/paste into a new Colab Notebook.

2. Create second code cell below where you pasted est_trans.py code.

3. Open main.py in a text editor and then copy/paste into the second code cell.

4. Once coding on the class estimate_transform is complete, copy the first cell and paste into est_trans.py or create a new est_trans.py and follow submission guidlines below.

5. DO NOT add any imports or do any type of viewing (matplotlib, cv2.imshow, etc) in the first code cell with the estimate_transforms class's code. YOU MAY GET A ZERO ON ALL CODE IF YOU DO THIS. Put this stuff in the main section.

Also, do not use any inline "!" bash commands in your first code cell where est_trans.py code is located. You wont need it and it will mess up the grading process, which will lose you points since you cant follow instructions.


## How To Submit
1. For submission replace the cvfa21netid part of the directory with your netid. In my case, my netid is danielsawyer so the directory name would be danielsawyer_pa-2

2. The whole project should be contained within that directory. Then zip the directory, and only that directory, then save it as netid_pa-2.zip where netid is replaced by your netid. In my case, it would be danielsawyer_pa-2.zip

3. The only 2 files in the netid_pa-2 directory should be est_trans.py and report.pdf

4. After creating the zip file, upload it to Canvas by the submission due date.

Here is an example tree of the directory structure you should be turning in with the netid being danielsawyer.

```
danielsawyer_pa-2.zip contains...
└── danielsawyer_pa-2
    ├── est_trans.py
    └── report.pdf
```