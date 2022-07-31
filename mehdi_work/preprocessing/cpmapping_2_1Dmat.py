# -*- coding: utf-8 -*-
"""
File to convert pressure coefficient data (chordwise evolution at one serial at one Y) to a 1D .mat file.

File used for pre-processing on the GPSS research framework.

Mehdi Anhichem
University of Liverpool
30/07/2022
"""

#==============================================================================
# IMPORT REQUIRED MODULES
#==============================================================================

import itertools
import numpy as np
import time
import pandas as pd

import os
import time
import random

barkla_path = '/users/anhichem/sharedscratch/programming'
working_path = barkla_path # To change according to working platform

main_path = working_path+'/gpss-research/mehdi_work/'
data_path = working_path+'/data'
test_path = working_path+'/gpss-research/mehdi_work/preprocessing' # To change according to acitivity
import_GP_for_AeroData_path = working_path+'/GP_for_AeroData'

import sys
sys.path.append(import_GP_for_AeroData_path)
import information_sources

# for reproducibility of this notebook:
rng = np.random.RandomState(123)
random.seed(123)

#==============================================================================
# GENERATING DATA
#==============================================================================
print('### Generating data from pressure taps information source ###')

IS_pressure_taps = information_sources.InformationSource(location = data_path)
IS_pressure_taps.get_pressure_taps(get_z = False)
IS_pressure_taps.info()

avail_serial = IS_pressure_taps.serials_available(False)
pressure_taps_data = IS_pressure_taps.df

print('### Data generation finished ###')

os.chdir(test_path)
print('### Filtering data at A =  3.01 ; M = 0.82 ###')
df_pressure_taps_serial = IS_pressure_taps.filter_serial(310)

# Remove one outlier
df_pressure_taps_serial = df_pressure_taps_serial.loc[(df_pressure_taps_serial['Cp']<1.0)]

# Data selection
pressure_taps_data_yfix = pressure_taps_data.loc[(pressure_taps_data['y']==574.4)]
X_t_yfix = pressure_taps_data_yfix['x'].values.reshape(-1,1)
Y_t_yfix = pressure_taps_data_yfix['Cp'].values.reshape(-1,1)
print(X_t_yfix.shape, Y_t_yfix.shape)

# Save as a .mat file
from scipy.io import savemat
mdic = {"X": X_t_yfix, "y": Y_t_yfix}
savemat("../data/test_1d.mat", mdic)

