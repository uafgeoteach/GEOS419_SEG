# GEOS419: Solid Earth Geophysics

A public GitHub repository within the organization [uafgeoteach](https://github.com/uafgeoteach). 
Contains materials for GEOS 419 Solid Earth Geophysics, a class at the University of Alaska Fairbanks by 
[Bryant Chow](https://bryantchow.com/) and [Carl Tape](https://sites.google.com/alaska.edu/carltape/)

Course Webpage: [GEOS 419](https://bryantchow.com/teaching/geos419)

This repository can be downloaded from GitHub with the following command:

```bash
git clone --depth=1 https://github.com/uafgeoteach/GEOS419_SEG.git
```

---

## SETUP
UAF students will run these notebooks within the OpenScienceLab setup at UAF and 
do not need to manually install or set up their own environments. However for those
that would like to run things locally, please follow the instructions below.

### Local Conda Environment

1. Install [miniconda](https://docs.conda.io/en/latest/miniconda.html) or [anaconda](https://www.anaconda.com/products/individual)
2. Navigate to the GEOS419_SEG directory
  ```bash
  cd GEOS419_SEG/setup
  ```
3. Create your Conda environment
  ```bash
  conda env create -f setup/geos419.yml
  ```
4. Activate the conda environment
  ```bash
  conda activate geos419
  ```
5. Launch jupyter lab
  ```bash
  cd ..
  jupyter lab
  ```
6. This should open a web browser interface where you can browse and run notebooks

7. Don't forget to deactive your Conda environment
   ```conda deactivate```