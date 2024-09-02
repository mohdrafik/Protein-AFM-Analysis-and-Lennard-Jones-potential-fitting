# this is main program start here ------------>
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.io as sio
import os
from termcolor import colored


from listxlsfilesinOrder import listxlsFiles
from  converdfSetAxisgetNumpyArray import readASdfsetaxisAmpasnp
from plotmatlabfun import plot_data
from reverseArrayOfAvgWindow import reverseArrayofAvgValuesWndsize
from detect_inflexiondy_dxZero import detect_inflexion_pointAfterAverage
from final_index_calculation import findActualInflexion
from inflexionMinimadownbump import findDownBump 
from fitselectdataRange1bymfind import find1bymcampdfandfit
from savefiledf2dat import filesaveDatain_dat

data_path =  "dataproblem\\"
amp_inOrder,Phase_inOrder = listxlsFiles(data_path)

for i in range(len(amp_inOrder)):
    filenameAmplitude = amp_inOrder[i]
    filenamephase = Phase_inOrder[i]
    print(f"I am dealing with file = {i+1}.")
#     readASdfsetaxisAmpasnp(data_path,filenameAmplitude,filenamephase)
    print(f"I have read and converted the data in dataframe and numpy array and no of row in amp as data_endamp for file {i+1} named as {filenameAmplitude} and {filenamephase}.")
    res = readASdfsetaxisAmpasnp(data_path,filenameAmplitude,filenamephase)
    ampdf = res[0]
    phasedf = res[1]
    data_endamp = res[2]
    ampdfPiezoColumnarr = res[3]
    ampdfAmplitudeColumnarr = res[4]
    
    plt.figure()
    plot_data(ampdf,label='amp',color='blue', marker='', markersize=1,alpha=0.8,title=f"amplitude Vs Piezo {i+1}th_data",Xaxis="Piezo",Yaxis='Amplitude')
    plt.show()
    
    plt.figure()
    plot_data(phasedf,label='phase',color='red', marker='', markersize=1,alpha=0.6,title=f"Phase Vs Piezo {i+1}th_data",Xaxis="Piezo",Yaxis='Phase')
    plt.show()
    avg_window =  3 #4 #7
    list_avg = reverseArrayofAvgValuesWndsize(ampdf,phasedf,avg_window)
    plt.figure()
    plot_data(list_avg,label=f"avg of {avg_window} ",title=f"avg plot of {avg_window} data points for {i+1} file")
    plt.show()
    consecutive_decrease_windowsize = 4 #5 #6
    index = detect_inflexion_pointAfterAverage(ampdf,list_avg,consecutive_decrease_windowsize) 
    inflexion_After_avg =  index
    print("index of inflexion point w.r.to the average list(i.e. in list_avg) :",inflexion_After_avg,"<-->")
    
       
    final_Actual_index = findActualInflexion(inflexion_After_avg,list_avg,data_endamp,avg_window,ampdfAmplitudeColumnarr,ampdfPiezoColumnarr)
    zero_orFlatAmp = final_Actual_index
    print(zero_orFlatAmp )
    print(ampdf.iloc[final_Actual_index,0])
    
    # <--------- it is for the finding the downbump in the actual data ... >
    res_indices = findDownBump(ampdf,zero_orFlatAmp)
    index_inflexion = res_indices[0]
    print("\n index_inflexion ---------->",index_inflexion)
    index_minima = res_indices[1]
    print("\n index_minima ---------->",index_minima)
    backward_MinimaBump_nmValue = 4.0
    forward_MinimaBump_nmValue = 10.0
    
#     (ampdata2saveAspiezo_nm,ampdata2saveAsAmplitude_nm,phasedata2savedegree)
    res_m = find1bymcampdfandfit(ampdf,phasedf,backward_MinimaBump_nmValue,forward_MinimaBump_nmValue,res_indices,data_endamp,i,part1=None,part2 =None)
    ampdata2saveAspiezo_nm = res_m[0]
    ampdata2saveAsAmplitude_nm = res_m[1]
    phasedata2savedegree = res_m[2]
    
    fdata_path = "dataproblem\\"
    directory_name = "processdata\\"
    directory_path = os.path.join(fdata_path,directory_name)
    if not os.path.exists(directory_path):
        # If not, create the directory
        os.makedirs(directory_path)
        print(f"Directory '{directory_name}' created successfully.")
    else:
        print(f"Directory '{directory_name}' already exists.")

    filesaveDatain_dat(directory_path,ampdata2saveAspiezo_nm,ampdata2saveAsAmplitude_nm,phasedata2savedegree,filenameAmplitude,filenamephase)  
    # plt.close(all)
    