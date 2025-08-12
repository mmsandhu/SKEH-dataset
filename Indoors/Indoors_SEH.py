"""
MIT License

Copyright (c) 2025 Moid Sandhu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
from scipy.signal import lfilter, lfilter_zi, filtfilt, butter
from statistics import mean 
from array import *
import random
import csv
from scipy.signal import find_peaks
from scipy import stats, optimize, interpolate
from statsmodels import robust
from scipy.stats import kurtosis
from scipy.stats import skew
import math 
from scipy.signal import periodogram, welch
from scipy.stats import entropy
from scipy.fftpack import fft, ifft
from scipy import signal
from scipy.signal import find_peaks


'''
INDOOR SEH Data
'''

path = '.../SKEH/Indoors/SEH/'

experiment_1_running = pd.read_csv(path+'Exp 1/running.csv')
experiment_1_sitting = pd.read_csv(path+'Exp 1/sitting.csv')
experiment_1_stairs = pd.read_csv(path+'Exp 1/stairs.csv')
experiment_1_standing = pd.read_csv(path+'Exp 1/standing.csv')
experiment_1_walking = pd.read_csv(path+'Exp 1/walking.csv')

experiment_2_running = pd.read_csv(path+'Exp 2/running.csv')
experiment_2_sitting = pd.read_csv(path+'Exp 2/sitting.csv')
experiment_2_stairs = pd.read_csv(path+'Exp 2/stairs.csv')
experiment_2_standing = pd.read_csv(path+'Exp 2/standing.csv')
experiment_2_walking = pd.read_csv(path+'Exp 2/walking.csv')

experiment_3_running = pd.read_csv(path+'Exp 3/running.csv')
experiment_3_sitting = pd.read_csv(path+'Exp 3/sitting.csv')
experiment_3_stairs = pd.read_csv(path+'Exp 3/stairs.csv')
experiment_3_standing = pd.read_csv(path+'Exp 3/standing.csv')
experiment_3_walking = pd.read_csv(path+'Exp 3/walking.csv')

experiment_4_running = pd.read_csv(path+'Exp 4/running.csv')
experiment_4_sitting = pd.read_csv(path+'Exp 4/sitting.csv')
experiment_4_stairs = pd.read_csv(path+'Exp 4/stairs.csv')
experiment_4_standing = pd.read_csv(path+'Exp 4/standing.csv')
experiment_4_walking = pd.read_csv(path+'Exp 4/walking.csv')

experiment_5_running = pd.read_csv(path+'Exp 5/running.csv')
experiment_5_sitting = pd.read_csv(path+'Exp 5/sitting.csv')
experiment_5_stairs = pd.read_csv(path+'Exp 5/stairs.csv')
experiment_5_standing = pd.read_csv(path+'Exp 5/standing.csv')
experiment_5_walking = pd.read_csv(path+'Exp 5/walking.csv')

experiment_6_running = pd.read_csv(path+'Exp 6/running.csv')
experiment_6_sitting = pd.read_csv(path+'Exp 6/sitting.csv')
experiment_6_stairs = pd.read_csv(path+'Exp 6/stairs.csv')
experiment_6_standing = pd.read_csv(path+'Exp 6/standing.csv')
experiment_6_walking = pd.read_csv(path+'Exp 6/walking.csv')

experiment_7_running = pd.read_csv(path+'Exp 7/running.csv')
experiment_7_sitting = pd.read_csv(path+'Exp 7/sitting.csv')
experiment_7_stairs = pd.read_csv(path+'Exp 7/stairs.csv')
experiment_7_standing = pd.read_csv(path+'Exp 7/standing.csv')
experiment_7_walking = pd.read_csv(path+'Exp 7/walking.csv')

experiment_8_running = pd.read_csv(path+'Exp 8/running.csv')
experiment_8_sitting = pd.read_csv(path+'Exp 8/sitting.csv')
experiment_8_stairs = pd.read_csv(path+'Exp 8/stairs.csv')
experiment_8_standing = pd.read_csv(path+'Exp 8/standing.csv')
experiment_8_walking = pd.read_csv(path+'Exp 8/walking.csv')

experiment_9_running = pd.read_csv(path+'Exp 9/running.csv')
experiment_9_sitting = pd.read_csv(path+'Exp 9/sitting.csv')
experiment_9_stairs = pd.read_csv(path+'Exp 9/stairs.csv')
experiment_9_standing = pd.read_csv(path+'Exp 9/standing.csv')
experiment_9_walking = pd.read_csv(path+'Exp 9/walking.csv')

experiment_10_running = pd.read_csv(path+'Exp 10/running.csv')
experiment_10_sitting = pd.read_csv(path+'Exp 10/sitting.csv')
experiment_10_stairs = pd.read_csv(path+'Exp 10/stairs.csv')
experiment_10_standing = pd.read_csv(path+'Exp 10/standing.csv')
experiment_10_walking = pd.read_csv(path+'Exp 10/walking.csv')

experiment_11_running = pd.read_csv(path+'Exp 11/running.csv')
experiment_11_sitting = pd.read_csv(path+'Exp 11/sitting.csv')
experiment_11_stairs = pd.read_csv(path+'Exp 11/stairs.csv')
experiment_11_standing = pd.read_csv(path+'Exp 11/standing.csv')
experiment_11_walking = pd.read_csv(path+'Exp 11/walking.csv')

experiment_12_running = pd.read_csv(path+'Exp 12/running.csv')
experiment_12_sitting = pd.read_csv(path+'Exp 12/sitting.csv')
experiment_12_stairs = pd.read_csv(path+'Exp 12/stairs.csv')
experiment_12_standing = pd.read_csv(path+'Exp 12/standing.csv')
experiment_12_walking = pd.read_csv(path+'Exp 12/walking.csv')

experiment_13_running = pd.read_csv(path+'Exp 13/running.csv')
experiment_13_sitting = pd.read_csv(path+'Exp 13/sitting.csv')
experiment_13_stairs = pd.read_csv(path+'Exp 13/stairs.csv')
experiment_13_standing = pd.read_csv(path+'Exp 13/standing.csv')
experiment_13_walking = pd.read_csv(path+'Exp 13/walking.csv')

experiment_14_running = pd.read_csv(path+'Exp 14/running.csv')
experiment_14_sitting = pd.read_csv(path+'Exp 14/sitting.csv')
experiment_14_stairs = pd.read_csv(path+'Exp 14/stairs.csv')
experiment_14_standing = pd.read_csv(path+'Exp 14/standing.csv')
experiment_14_walking = pd.read_csv(path+'Exp 14/walking.csv')

experiment_15_running = pd.read_csv(path+'Exp 15/running.csv')
experiment_15_sitting = pd.read_csv(path+'Exp 15/sitting.csv')
experiment_15_stairs = pd.read_csv(path+'Exp 15/stairs.csv')
experiment_15_standing = pd.read_csv(path+'Exp 15/standing.csv')
experiment_15_walking = pd.read_csv(path+'Exp 15/walking.csv')

experiment_16_running = pd.read_csv(path+'Exp 16/running.csv')
experiment_16_sitting = pd.read_csv(path+'Exp 16/sitting.csv')
experiment_16_stairs = pd.read_csv(path+'Exp 16/stairs.csv')
experiment_16_standing = pd.read_csv(path+'Exp 16/standing.csv')
experiment_16_walking = pd.read_csv(path+'Exp 16/walking.csv')

experiment_17_running = pd.read_csv(path+'Exp 17/running.csv')
experiment_17_sitting = pd.read_csv(path+'Exp 17/sitting.csv')
experiment_17_stairs = pd.read_csv(path+'Exp 17/stairs.csv')
experiment_17_standing = pd.read_csv(path+'Exp 17/standing.csv')
experiment_17_walking = pd.read_csv(path+'Exp 17/walking.csv')

experiment_18_running = pd.read_csv(path+'Exp 18/running.csv')
experiment_18_sitting = pd.read_csv(path+'Exp 18/sitting.csv')
experiment_18_stairs = pd.read_csv(path+'Exp 18/stairs.csv')
experiment_18_standing = pd.read_csv(path+'Exp 18/standing.csv')
experiment_18_walking = pd.read_csv(path+'Exp 18/walking.csv')

experiment_19_running = pd.read_csv(path+'Exp 19/running.csv')
experiment_19_sitting = pd.read_csv(path+'Exp 19/sitting.csv')
experiment_19_stairs = pd.read_csv(path+'Exp 19/stairs.csv')
experiment_19_standing = pd.read_csv(path+'Exp 19/standing.csv')
experiment_19_walking = pd.read_csv(path+'Exp 19/walking.csv')



'''
Remove samples with less than zero values
'''
experiment_1_running.drop(experiment_1_running[experiment_1_running['Data'] < 0].index, inplace = True)
experiment_2_running.drop(experiment_2_running[experiment_2_running['Data'] < 0].index, inplace = True)
experiment_3_running.drop(experiment_3_running[experiment_3_running['Data'] < 0].index, inplace = True)
experiment_4_running.drop(experiment_4_running[experiment_4_running['Data'] < 0].index, inplace = True)
experiment_5_running.drop(experiment_5_running[experiment_5_running['Data'] < 0].index, inplace = True)
experiment_6_running.drop(experiment_6_running[experiment_6_running['Data'] < 0].index, inplace = True)
experiment_7_running.drop(experiment_7_running[experiment_7_running['Data'] < 0].index, inplace = True)
experiment_8_running.drop(experiment_8_running[experiment_8_running['Data'] < 0].index, inplace = True)
experiment_9_running.drop(experiment_9_running[experiment_9_running['Data'] < 0].index, inplace = True)
experiment_10_running.drop(experiment_10_running[experiment_10_running['Data'] < 0].index, inplace = True)
experiment_11_running.drop(experiment_11_running[experiment_11_running['Data'] < 0].index, inplace = True)
experiment_12_running.drop(experiment_12_running[experiment_12_running['Data'] < 0].index, inplace = True)
experiment_13_running.drop(experiment_13_running[experiment_13_running['Data'] < 0].index, inplace = True)
experiment_14_running.drop(experiment_14_running[experiment_14_running['Data'] < 0].index, inplace = True)
experiment_15_running.drop(experiment_15_running[experiment_15_running['Data'] < 0].index, inplace = True)
experiment_16_running.drop(experiment_16_running[experiment_16_running['Data'] < 0].index, inplace = True)
experiment_17_running.drop(experiment_17_running[experiment_17_running['Data'] < 0].index, inplace = True)
experiment_18_running.drop(experiment_18_running[experiment_18_running['Data'] < 0].index, inplace = True)
experiment_19_running.drop(experiment_19_running[experiment_19_running['Data'] < 0].index, inplace = True)

experiment_1_sitting.drop(experiment_1_sitting[experiment_1_sitting['Data'] < 0].index, inplace = True)
experiment_2_sitting.drop(experiment_2_sitting[experiment_2_sitting['Data'] < 0].index, inplace = True)
experiment_3_sitting.drop(experiment_3_sitting[experiment_3_sitting['Data'] < 0].index, inplace = True)
experiment_4_sitting.drop(experiment_4_sitting[experiment_4_sitting['Data'] < 0].index, inplace = True)
experiment_5_sitting.drop(experiment_5_sitting[experiment_5_sitting['Data'] < 0].index, inplace = True)
experiment_6_sitting.drop(experiment_6_sitting[experiment_6_sitting['Data'] < 0].index, inplace = True)
experiment_7_sitting.drop(experiment_7_sitting[experiment_7_sitting['Data'] < 0].index, inplace = True)
experiment_8_sitting.drop(experiment_8_sitting[experiment_8_sitting['Data'] < 0].index, inplace = True)
experiment_9_sitting.drop(experiment_9_sitting[experiment_9_sitting['Data'] < 0].index, inplace = True)
experiment_10_sitting.drop(experiment_10_sitting[experiment_10_sitting['Data'] < 0].index, inplace = True)
experiment_11_sitting.drop(experiment_11_sitting[experiment_11_sitting['Data'] < 0].index, inplace = True)
experiment_12_sitting.drop(experiment_12_sitting[experiment_12_sitting['Data'] < 0].index, inplace = True)
experiment_13_sitting.drop(experiment_13_sitting[experiment_13_sitting['Data'] < 0].index, inplace = True)
experiment_14_sitting.drop(experiment_14_sitting[experiment_14_sitting['Data'] < 0].index, inplace = True)
experiment_15_sitting.drop(experiment_15_sitting[experiment_15_sitting['Data'] < 0].index, inplace = True)
experiment_16_sitting.drop(experiment_16_sitting[experiment_16_sitting['Data'] < 0].index, inplace = True)
experiment_17_sitting.drop(experiment_17_sitting[experiment_17_sitting['Data'] < 0].index, inplace = True)
experiment_18_sitting.drop(experiment_18_sitting[experiment_18_sitting['Data'] < 0].index, inplace = True)
experiment_19_sitting.drop(experiment_19_sitting[experiment_19_sitting['Data'] < 0].index, inplace = True)

experiment_1_stairs.drop(experiment_1_stairs[experiment_1_stairs['Data'] < 0].index, inplace = True)
experiment_2_stairs.drop(experiment_2_stairs[experiment_2_stairs['Data'] < 0].index, inplace = True)
experiment_3_stairs.drop(experiment_3_stairs[experiment_3_stairs['Data'] < 0].index, inplace = True)
experiment_4_stairs.drop(experiment_4_stairs[experiment_4_stairs['Data'] < 0].index, inplace = True)
experiment_5_stairs.drop(experiment_5_stairs[experiment_5_stairs['Data'] < 0].index, inplace = True)
experiment_6_stairs.drop(experiment_6_stairs[experiment_6_stairs['Data'] < 0].index, inplace = True)
experiment_7_stairs.drop(experiment_7_stairs[experiment_7_stairs['Data'] < 0].index, inplace = True)
experiment_8_stairs.drop(experiment_8_stairs[experiment_8_stairs['Data'] < 0].index, inplace = True)
experiment_9_stairs.drop(experiment_9_stairs[experiment_9_stairs['Data'] < 0].index, inplace = True)
experiment_10_stairs.drop(experiment_10_stairs[experiment_10_stairs['Data'] < 0].index, inplace = True)
experiment_11_stairs.drop(experiment_11_stairs[experiment_11_stairs['Data'] < 0].index, inplace = True)
experiment_12_stairs.drop(experiment_12_stairs[experiment_12_stairs['Data'] < 0].index, inplace = True)
experiment_13_stairs.drop(experiment_13_stairs[experiment_13_stairs['Data'] < 0].index, inplace = True)
experiment_14_stairs.drop(experiment_14_stairs[experiment_14_stairs['Data'] < 0].index, inplace = True)
experiment_15_stairs.drop(experiment_15_stairs[experiment_15_stairs['Data'] < 0].index, inplace = True)
experiment_16_stairs.drop(experiment_16_stairs[experiment_16_stairs['Data'] < 0].index, inplace = True)
experiment_17_stairs.drop(experiment_17_stairs[experiment_17_stairs['Data'] < 0].index, inplace = True)
experiment_18_stairs.drop(experiment_18_stairs[experiment_18_stairs['Data'] < 0].index, inplace = True)
experiment_19_stairs.drop(experiment_19_stairs[experiment_19_stairs['Data'] < 0].index, inplace = True)

experiment_1_standing.drop(experiment_1_standing[experiment_1_standing['Data'] < 0].index, inplace = True)
experiment_2_standing.drop(experiment_2_standing[experiment_2_standing['Data'] < 0].index, inplace = True)
experiment_3_standing.drop(experiment_3_standing[experiment_3_standing['Data'] < 0].index, inplace = True)
experiment_4_standing.drop(experiment_4_standing[experiment_4_standing['Data'] < 0].index, inplace = True)
experiment_5_standing.drop(experiment_5_standing[experiment_5_standing['Data'] < 0].index, inplace = True)
experiment_6_standing.drop(experiment_6_standing[experiment_6_standing['Data'] < 0].index, inplace = True)
experiment_7_standing.drop(experiment_7_standing[experiment_7_standing['Data'] < 0].index, inplace = True)
experiment_8_standing.drop(experiment_8_standing[experiment_8_standing['Data'] < 0].index, inplace = True)
experiment_9_standing.drop(experiment_9_standing[experiment_9_standing['Data'] < 0].index, inplace = True)
experiment_10_standing.drop(experiment_10_standing[experiment_10_standing['Data'] < 0].index, inplace = True)
experiment_11_standing.drop(experiment_11_standing[experiment_11_standing['Data'] < 0].index, inplace = True)
experiment_12_standing.drop(experiment_12_standing[experiment_12_standing['Data'] < 0].index, inplace = True)
experiment_13_standing.drop(experiment_13_standing[experiment_13_standing['Data'] < 0].index, inplace = True)
experiment_14_standing.drop(experiment_14_standing[experiment_14_standing['Data'] < 0].index, inplace = True)
experiment_15_standing.drop(experiment_15_standing[experiment_15_standing['Data'] < 0].index, inplace = True)
experiment_16_standing.drop(experiment_16_standing[experiment_16_standing['Data'] < 0].index, inplace = True)
experiment_17_standing.drop(experiment_17_standing[experiment_17_standing['Data'] < 0].index, inplace = True)
experiment_18_standing.drop(experiment_18_standing[experiment_18_standing['Data'] < 0].index, inplace = True)
experiment_19_standing.drop(experiment_19_standing[experiment_19_standing['Data'] < 0].index, inplace = True)

experiment_1_walking.drop(experiment_1_walking[experiment_1_walking['Data'] < 0].index, inplace = True)
experiment_2_walking.drop(experiment_2_walking[experiment_2_walking['Data'] < 0].index, inplace = True)
experiment_3_walking.drop(experiment_3_walking[experiment_3_walking['Data'] < 0].index, inplace = True)
experiment_4_walking.drop(experiment_4_walking[experiment_4_walking['Data'] < 0].index, inplace = True)
experiment_5_walking.drop(experiment_5_walking[experiment_5_walking['Data'] < 0].index, inplace = True)
experiment_6_walking.drop(experiment_6_walking[experiment_6_walking['Data'] < 0].index, inplace = True)
experiment_7_walking.drop(experiment_7_walking[experiment_7_walking['Data'] < 0].index, inplace = True)
experiment_8_walking.drop(experiment_8_walking[experiment_8_walking['Data'] < 0].index, inplace = True)
experiment_9_walking.drop(experiment_9_walking[experiment_9_walking['Data'] < 0].index, inplace = True)
experiment_10_walking.drop(experiment_10_walking[experiment_10_walking['Data'] < 0].index, inplace = True)
experiment_11_walking.drop(experiment_11_walking[experiment_11_walking['Data'] < 0].index, inplace = True)
experiment_12_walking.drop(experiment_12_walking[experiment_12_walking['Data'] < 0].index, inplace = True)
experiment_13_walking.drop(experiment_13_walking[experiment_13_walking['Data'] < 0].index, inplace = True)
experiment_14_walking.drop(experiment_14_walking[experiment_14_walking['Data'] < 0].index, inplace = True)
experiment_15_walking.drop(experiment_15_walking[experiment_15_walking['Data'] < 0].index, inplace = True)
experiment_16_walking.drop(experiment_16_walking[experiment_16_walking['Data'] < 0].index, inplace = True)
experiment_17_walking.drop(experiment_17_walking[experiment_17_walking['Data'] < 0].index, inplace = True)
experiment_18_walking.drop(experiment_18_walking[experiment_18_walking['Data'] < 0].index, inplace = True)
experiment_19_walking.drop(experiment_19_walking[experiment_19_walking['Data'] < 0].index, inplace = True)



'''
Combining data from 5 classess from all experiments
'''
aa = [experiment_1_running['Data'].values, experiment_2_running['Data'].values, experiment_3_running['Data'].values, experiment_4_running['Data'].values, experiment_5_running['Data'].values, 
      experiment_6_running['Data'].values, experiment_7_running['Data'].values, experiment_8_running['Data'].values, experiment_9_running['Data'].values, experiment_10_running['Data'].values, 
      experiment_11_running['Data'].values, experiment_12_running['Data'].values, experiment_13_running['Data'].values, experiment_14_running['Data'].values, experiment_15_running['Data'].values, 
      experiment_16_running['Data'].values, experiment_17_running['Data'].values, experiment_18_running['Data'].values, experiment_19_running['Data'].values]
running_data = np.concat(aa)
bb = [experiment_1_sitting['Data'].values, experiment_2_sitting['Data'].values, experiment_3_sitting['Data'].values, experiment_4_sitting['Data'].values, experiment_5_sitting['Data'].values, 
      experiment_6_sitting['Data'].values, experiment_7_sitting['Data'].values, experiment_8_sitting['Data'].values, experiment_9_sitting['Data'].values, experiment_10_sitting['Data'].values, 
      experiment_11_sitting['Data'].values, experiment_12_sitting['Data'].values, experiment_13_sitting['Data'].values, experiment_14_sitting['Data'].values, experiment_15_sitting['Data'].values, 
      experiment_16_sitting['Data'].values, experiment_17_sitting['Data'].values, experiment_18_sitting['Data'].values, experiment_19_sitting['Data'].values]
sitting_data = np.concat(bb)
cc = [experiment_1_stairs['Data'].values, experiment_2_stairs['Data'].values, experiment_3_stairs['Data'].values, experiment_4_stairs['Data'].values, experiment_5_stairs['Data'].values, 
      experiment_6_stairs['Data'].values, experiment_7_stairs['Data'].values, experiment_8_stairs['Data'].values, experiment_9_stairs['Data'].values, experiment_10_stairs['Data'].values, 
      experiment_11_stairs['Data'].values, experiment_12_stairs['Data'].values, experiment_13_stairs['Data'].values, experiment_14_stairs['Data'].values, experiment_15_stairs['Data'].values, 
      experiment_16_stairs['Data'].values, experiment_17_stairs['Data'].values, experiment_18_stairs['Data'].values, experiment_19_stairs['Data'].values]
stairs_data = np.concat(cc)
dd = [experiment_1_standing['Data'].values, experiment_2_standing['Data'].values, experiment_3_standing['Data'].values, experiment_4_standing['Data'].values, experiment_5_standing['Data'].values, 
      experiment_6_standing['Data'].values, experiment_7_standing['Data'].values, experiment_8_standing['Data'].values, experiment_9_standing['Data'].values, experiment_10_standing['Data'].values, 
      experiment_11_standing['Data'].values, experiment_12_standing['Data'].values, experiment_13_standing['Data'].values, experiment_14_standing['Data'].values, experiment_15_standing['Data'].values, 
      experiment_16_standing['Data'].values, experiment_17_standing['Data'].values, experiment_18_standing['Data'].values, experiment_19_standing['Data'].values]
standing_data = np.concat(dd)
ee = [experiment_1_walking['Data'].values, experiment_2_walking['Data'].values, experiment_3_walking['Data'].values, experiment_4_walking['Data'].values, experiment_5_walking['Data'].values, 
      experiment_6_walking['Data'].values, experiment_7_walking['Data'].values, experiment_8_walking['Data'].values, experiment_9_walking['Data'].values, experiment_10_walking['Data'].values, 
      experiment_11_walking['Data'].values, experiment_12_walking['Data'].values, experiment_13_walking['Data'].values, experiment_14_walking['Data'].values, experiment_15_walking['Data'].values, 
      experiment_16_walking['Data'].values, experiment_17_walking['Data'].values, experiment_18_walking['Data'].values, experiment_19_walking['Data'].values]
walking_data = np.concat(ee)





'''
Reducing the sampling rate (if needed) 
'''
# new_sampling_rate = 100
# #own_sampling_factor = 5
# current_sampling_rate = 100
# down_ratio = current_sampling_rate/new_sampling_rate
# from scipy import signal
# running_data = signal.resample(running_data, int(len(running_data)/down_ratio))
# sitting_data = signal.resample(sitting_data, int(len(sitting_data)/down_ratio))
# stairs_data = signal.resample(stairs_data, int(len(stairs_data)/down_ratio))
# standing_data = signal.resample(standing_data, int(len(standing_data)/down_ratio))
# walking_data = signal.resample(walking_data, int(len(walking_data)/down_ratio))


