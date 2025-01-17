# -*- coding: utf-8 -*-
"""
File to convert pressure coefficient data (chordwise evolution at one serial at one Y
with experimental conditions variations) to a 3D .mat file.

File used for pre-processing on the GPSS research framework.

Mehdi Anhichem
University of Liverpool
24/08/2022
"""

#==============================================================================
# IMPORT REQUIRED MODULES
#==============================================================================

import numpy as np
import os
import random
import matplotlib.pyplot as plt

barkla_path = '/users/anhichem/sharedscratch/programming'
local_path = 'C:/Users/anhichem/Documents/00-LIVERPOOL_UNI/10-Programming/01-Project/'

working_path = local_path # To change according to working platform

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

# Remove Mach = 0
pressure_taps_data = pressure_taps_data.loc[(pressure_taps_data['Mach']>0.1)]

# Remove one outlier
pressure_taps_data = pressure_taps_data.loc[(pressure_taps_data['Cp']<1.0)]

# Data selection
pressure_taps_data_yfix = pressure_taps_data.loc[(pressure_taps_data['y']==574.4)]
X_t_yfix = pressure_taps_data_yfix[['alpha', 'Mach', 'x']]
Y_t_yfix = pressure_taps_data_yfix['Cp'].values.reshape(-1,1)
print(X_t_yfix.shape, Y_t_yfix.shape)

# Save as a .mat file
from scipy.io import savemat
mdic = {"X": X_t_yfix, "y": Y_t_yfix}
savemat("../data/3d/data_3d_y574_4.mat", mdic)

