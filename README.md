# GEOS419_SEG

A public GitHub repository within the organization
[uafgeoteach](https://github.com/uafgeoteach). Contains materials for GEOS 419 Solid Earth Geophysics, a class at the University of Alaska Fairbanks by [Bryant Chow](https://bryantchow.com/) and [Carl Tape](https://sites.google.com/alaska.edu/carltape/)

Course webpage: [GEOS 419]

The repository can be obtained from GitHub with this command:
```
git clone --depth=1 https://github.com/uafgeoteach/GEOS419_SEG.git
```

UAF students will run these notebooks within the OpenScienceLab setup at UAF.

### Setup
---
A `.yml` file (see setup/ folder) lists dependencies. This file, executed within conda or docker, enables a user to establish the software tools needed to execute the iPython notebooks.

### How to run using Conda
---

- install conda (miniconda or anaconda, former recommended) if not done already
- navigate to the setup folder
  ```bash
  cd GEOS419_SEG/setup
  ```
- setup the conda environment
  ```bash
  conda env create -f geos419.yml
  ```
- activate the conda environment once the setup is complete
  ```bash
  conda activate geos419
  ```
- navigate back to the root of repository and launch jupyter
  ```bash
  cd ..
  jupyter lab
  ```
- browse and run notebooks as desired
