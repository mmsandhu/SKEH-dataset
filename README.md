# SKEH-dataset
This is Solar and Kinetic Energy Harvesting (SKEH) dataset for human activity recognition. This dataset captures information from synchronized solar and kinetic energy harvesters as well as inertial sensors under diverse activity patterns. <br>

**Data Collection**

**Sensors Used:**

**Kinetic energy harvester:** MIDÉ Technology S230-J1FR-1808XB two-layer piezoelectric bending transducer.

**Solar energy harvester:** IXYS SLMD121H10L solar module

**Accelerometer:** InvenSense MPU9250


All data stored at **100 Hz.**

**Data Collection Device (SEH and KEH):** Beaglebone Green

**Collection Period:** From November 2018 to June 2022

**Environment:** Indoor and outdoor

**Collection Protocol:** Data during 5 activities from each participant 



Dataset Structure:

**The data is organised in 2 folders:**

Indoors

Outdoors

**Each folder has three subfolders:**

Accelerometer

KEH

SEH


**Five files** in each folder (running.csv, sitting.csv, stairs.csv, standing.csv, walking.csv)

**File Formats:** CSV for time-series data

**Data Schema: **

Kinetic energy harvester:

`Data`: [Ampere]

Solar energy harvester:

`Data`: [Ampere]

Accelerometer:

`acc_x`: [g]

`acc_y`: [g]

`acc_z`: [g]


<br>
**Raw Data Status:** This is raw data segmented into 5 activities (break period were removed).

**Preprocessing Steps:**

**Resampling:** Solar and kinetic energy harvesting data was downsampled from 100 kHz to 100 Hz using linear interpolation.

**Segmentation:** Data was segmented into 5 activities and break periods were removed.


<br>
**Link to Data:**

https://data.csiro.au/collection/csiro:65940



<br>
**Please cite the relevant work.**

1- Sandhu, Muhammad Moid, et al. "Fusedar: Energy-positive human activity recognition using kinetic and solar signal fusion." IEEE Sensors Journal 23.11 (2023): 12411-12426.

2- Sandhu, Muhammad Moid, et al. Self-Powered Internet of Things: How Energy Harvesters Can Enable Energy-Positive Sensing, Processing, and Communication. Springer Nature, 2023.

3- Sandhu, Muhammad Moid, et al. "SolAR: Energy positive human activity recognition using solar cells." 2021 IEEE International Conference on Pervasive Computing and Communications (PerCom). IEEE, 2021.


