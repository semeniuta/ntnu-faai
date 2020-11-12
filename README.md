# ntnu-faai

Code examples for the seminars in the course [TØL4204 - Flexible Automation and Artificial Intelligence](https://www.ntnu.edu/studies/courses/T%C3%98L4204#tab=omEmnet) at NTNU. 

## Commands

To create a new `conda` environment based on the specification file:

```
conda env create -f cv-env.yml
```

To fetch all the files in Git submodules (dependencies in `libraries` directory):

```
git pull --recurse-submodules
git submodule update --init --recursive
```