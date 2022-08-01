# -*- coding: utf-8 -*-
"""
File used for running experiment py file on the GPSS research framework.

Mehdi Anhichem
University of Liverpool
31/07/2022
"""

#==============================================================================
# IMPORT REQUIRED MODULES
#==============================================================================
import numpy as np
import os

barkla_path = '/users/anhichem/sharedscratch/programming'
working_path = barkla_path # To change according to working platform

run_experiment_path = working_path+'/gpss-research/mehdi_work/'
import_experiment_path = working_path+'/gpss-research/source/'
import sys
sys.path.append(import_experiment_path)
import experiment

#==============================================================================
# RUN EXPERIMENT
#==============================================================================
os.chdir(run_experiment_path)
experiment.run_experiment_file('test_1d.py')
