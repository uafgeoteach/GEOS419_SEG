# GEOS419: Solid Earth Geophysics

A public GitHub repository within the organization [uafgeoteach](https://github.com/uafgeoteach). 
Contains materials for GEOS 419 Solid Earth Geophysics, a class at the University of Alaska Fairbanks by 
[Bryant Chow](https://bryantchow.com/) and [Carl Tape](https://sites.google.com/alaska.edu/carltape/)

Course Webpage: [GEOS 419](https://bryantchow.com/teaching/geos419)

This repository can be downloaded from GitHub with the following command:

```bash
git clone --depth=1 https://github.com/uafgeoteach/GEOS419_SEG.git
```

## Setup
UAF students will run these notebooks within the 
[OpenScienceLab](https://opensciencelab.asf.alaska.edu/portal/hub/login) environment at
 UAF and do not need to manually install or set up their own environments. For advanced 
users who would like to run things on their own computers, please follow the instructions below.

### Installing to Local Conda Environment

1. Install [miniconda](https://docs.conda.io/en/latest/miniconda.html) or [anaconda](https://www.anaconda.com/products/individual)
2. Clone the GEOS419\_SEG respository to wherever you store GitHub repositories
```bash
git clone --depth=1 https://github.com/uafgeoteach/GEOS419_SEG.git
```
3. Navigate to the GEOS419\_SEG directory
  ```bash
  cd GEOS419_SEG
  ```
4. Create your Conda environment from the course environment file
  ```bash
  conda env create -f setup/geos419.yml
  ```
5. Activate the conda environment
  ```bash
  conda activate geos419
  ```
6. Launch jupyter lab
  ```bash
  jupyter lab
  ```
8. This should open a web browser interface where you can browse and run 
   notebooks. 

9. Once you are done, make sure to save your progress and then close out of the 
   browesr. Don't forget to deactive your Conda environment
   ```bash
   conda deactivate
   ```
   
