# Clean Cells

Python module to delete the '# In [ ]' comments created when downloading a 
jupyter notebook file as a python file.

## Usage:

python CleanCells.py file

Where file is the location (full or relative path) of the downloaded .py file.

## Note:

This will also delete the comment '# coding utf-8' created by jupyter.

Possibly, future versions of the notebook will have differend headers or 
cell comments. This module will then be deprecated unless otherwise noted here.

## Warning:

This module will delete all comments that start with '# In[', 
which is the way jupyter writes its cells.
In case you have an actual comment in your code that should continue there,
you can change the way the comment starts or hack the module here in function
clean_cells().

## Updates:

- Jan 2017: Working with jupyter-notebook, not tested for ipython notebooks.