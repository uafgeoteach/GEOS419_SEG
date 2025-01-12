# GEOS419 Lab 1: Intro to Python

## Setup

We will run OpenScienceLab from a browser on our computer

1. Sign up for an ASF OpenScienceLab account here: https://opensciencelab.asf.alaska.edu/portal/hub/signup
2. To sign in with multifactor authentication, you will need an authenticator app on your phone, we suggest: Google Authenticator
3. Sign in to ASF OpenScienceLab with your account and MFA code
4. At the bottom of the 'Welcome' page, you should see a `GEOS419` block, click the `Go to lab` button
5. On the following page, click the `Start My Server` button
6. From the available Server Options, select: 'm6a.large - Single User', and click `Start`
5. Startup of the Jupyter Lab environment may take up to a few minutes

## Jupyter Lab

Once you have successfully accessed your JupyterLab environment, we will clone our first lab

1. In JupyterLab, click the `Terminal` icon (in section 'Other', a black box with a `$_` symbol inside)
2. In the newly-opened Terminal window, copy-paste the following command to clone our class repository

```bash
	git clone https://github.com/uafgeoteach/GEOS419_SEG.git
```

3. Type 'Yes' if prompted during the cloning process
4. Once cloned, you can access the repository from the directory window on the left-hand side of the browser
5. Double-click `GEOS419_SEG` > `lab1_intro_python` > `geos419_lab1_notebook1.ipynb`
6. This will open up a Jupyter notebook containing our first computer lab exercise

## Jupyter Notebook

Inside the Jupyter notebook, read along through the text and interact with the cells where possible.
Some cells are left intentionally blank, and are for you to input your own code.
A few tips and tricks for running notebooks include:

- **Run cells** one-by-one by hitting the $\blacktriangleright$ button at the top, or by hitting `Shift + Enter`
- **Run all cells** by hitting the $\blacktriangleright\blacktriangleright$ button at the top, or by running `Run -> Run All Cells`
- **Currently running cells** that are still processing will have a `[*]` symbol next to them
- **Finished cells** will have a `[1]` symbol next to them. The number inside the brackets represents what order this cell has been run in.
- Commands that start with `!` are Bash commands (i.e., commands you would run from the terminal)
- Commands that start with `%` are Jupyter Magic commands.
