import numpy as np 
import pandas as pd
import os
import matplotlib.pyplot as plt
from converdfSetAxisgetNumpyArray import readASdfsetaxisAmpasnp

def calculate_avg_wndsize(data_path,sameNo_of_amp_phase_length,amp_inOrder,Phase_inOrder,point_density_OLd,avg_windowsize):
    """ 
    this function to calculate the average size window for all the same type of file at once. 
    Data taken using the same setting then employing this function,
    we can get a accurate average window size, which is suitable for identifyig the downbump,inflexion and start of the flat region (zero_orFlatAmp) in data.

    """


    file_No = 0 
    all_value_amp_piezo = []

    for i in range(sameNo_of_amp_phase_length):
        filenameAmplitude = amp_inOrder[i]
        filenamephase = Phase_inOrder[i]
        file_No = i+1     

        print("\n",f"<----- IN process with files {filenameAmplitude} and {filenamephase} and file No. {file_No} -------->")

        print("\n",f"I am dealing with file = {file_No}.")
    #     readASdfsetaxisAmpasnp(data_path,filenameAmplitude,filenamephase)
        print(f"I have read and converted the data in dataframe and numpy array and no of row in amp as data_endamp for file {i+1} named as {filenameAmplitude} and {filenamephase}.")
        res = readASdfsetaxisAmpasnp(data_path,filenameAmplitude,filenamephase)
        ampdf = res[0]        # ampdf is two column dataframe with title: ['Piezo','Amplitude']
        phasedf = res[1]      # phasedf is two column dataframe with title: ['Piezo','Phase']
        data_endamp = res[2]   #  total length of ampdf, index of the last value is --> data_endamp-1
        ampdfPiezoColumnarr = res[3]  # it is single column Piezo numpy array  only
        ampdfAmplitudeColumnarr = res[4]    # it is single column  amplitude numpy array only
        A0 = res[5]    # A0 is the last value of the ampdf Amplitude


        ampdfPiezoColumnarr = ampdfPiezoColumnarr[0:]
        all_value_amp_piezo.extend(ampdfPiezoColumnarr)
    # all_value_amp_piezo  # list, this has whole piezo data values.

    all_value_amp_piezo_array = np.array(all_value_amp_piezo) # now numpy array 
    total_elements_IN_arrayof_allfiles = all_value_amp_piezo_array.shape[0]

    piezo_array_range = np.max(all_value_amp_piezo_array) - np.min(all_value_amp_piezo_array)
    # piezo_array_range
    no_of_points_IN_onedatafile  = (all_value_amp_piezo_array.shape[0])/(file_No)
    print(f"piezo array range:{piezo_array_range}, no_of_points_IN_onedatafile:{no_of_points_IN_onedatafile} and file_no.:{file_No}")
    # point_density_OLd = no_of_points_IN_onedatafile/piezo_array_range 
    point_density_Current = no_of_points_IN_onedatafile/piezo_array_range 

    if point_density_Current > point_density_OLd:
        scalar_factor_avgwndsize = point_density_Current/point_density_OLd 
        avg_window_current =  avg_windowsize*scalar_factor_avgwndsize
        avg_window_current = int(avg_window_current)
    else:
        scalar_factor_avgwndsize = point_density_OLd/point_density_Current 
        avg_window_current =  avg_windowsize/scalar_factor_avgwndsize
        avg_window_current = int(avg_window_current)
    
    return avg_window_current
# 8910.417881801475


def calculate_avg_wndsize_Individual_filewise(ampdfPiezoColumnarr,file_No,point_density_OLd,avg_windowsize):
    """ 
    this function to calculate the average size window for each file individually. 
    Data taken using the same setting then employing this function,
    we can get a accurate average window size, which is suitable for identifyig the downbump,inflexion and start of the flat region (zero_orFlatAmp) in data.
     
    """

    all_value_amp_piezo_array = ampdfPiezoColumnarr[0:]   # all_value_amp_piezo  # list, this has whole piezo data values.  

    # all_value_amp_piezo_array = np.array(all_value_amp_p iezo) # now numpy array
    total_elements_IN_arrayof_allfiles = all_value_amp_piezo_array.shape[0]

    piezo_array_range = np.max(all_value_amp_piezo_array) - np.min(all_value_amp_piezo_array)
    # piezo_array_range
    no_of_points_IN_onedatafile  = (all_value_amp_piezo_array.shape[0])
    print(f"piezo array range:{piezo_array_range}, no_of_points_IN_onedatafile:{no_of_points_IN_onedatafile} and individual file file_no.:{file_No}")
    # point_density_OLd = no_of_points_IN_onedatafile/piezo_array_range 
    point_density_Current = no_of_points_IN_onedatafile/piezo_array_range 

    if point_density_Current > point_density_OLd:
        scalar_factor_avgwndsize = point_density_Current/point_density_OLd 
        avg_window_current =  avg_windowsize*scalar_factor_avgwndsize
        avg_window_current = int(avg_window_current)
    else:
        scalar_factor_avgwndsize = point_density_OLd/point_density_Current 
        avg_window_current =  avg_windowsize/scalar_factor_avgwndsize
        avg_window_current = int(avg_window_current)
    
    return avg_window_current

