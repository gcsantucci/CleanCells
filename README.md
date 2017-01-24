# Clean Cells

Python module to delete the '# In[]' comments created when downloading a 
jupyter notebook file as a python file.

## Usage:

python CleanCells.py [file]

Where file is the location (full or relative path) of the downloaded .py file.

## Note:

This will also delete the comment '# coding utf-8' created by jupyter.
Possibly, future versions of the notebook will have differend headers or 
cell comments. This module will then be deprecated unless otherwise noted here.

## Updates:

- Jan 2017: Working with jupyter-notebook, not tested for ipython notebooks.