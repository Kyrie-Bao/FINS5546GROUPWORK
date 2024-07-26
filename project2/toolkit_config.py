""" toolkit_config.py
Project configuration file
"""


import os

# Determine the home directory based on the operating system
HOME_DIR = os.path.expanduser('~')

# Project directory relative to the home directory
PRJDIR = os.path.join(HOME_DIR, 'Documents', 'GitHub', 'FINS5546GROUPWORK')

# Data directory within the project directory
DATADIR = os.path.join(PRJDIR, 'data')