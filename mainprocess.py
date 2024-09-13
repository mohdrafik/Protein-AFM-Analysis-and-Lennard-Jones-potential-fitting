# this is main_process_file  ------------>
# this is main program start here ------------>

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.io as sio
import os
from termcolor import colored
import logging  

from shapeTr import tree 

from listxlsfilesinOrder import listxlsFiles
from converdfSetAxisgetNumpyArray import readASdfsetaxisAmpasnp
from plotmatlabfun import plot_data
from reverseArrayOfAvgWindow import reverseArrayofAvgValuesWndsize
from detect_inflexiondy_dxZero import detect_inflexion_pointAfterAverage
from final_index_calculation import findActualInflexion
import average_windowsize as avgws
import inflexionMinimadownbump as smfitbp 
import fitselectdataRange1bymfind as fitsmoothsave
# from savefiledf2dat import filesaveDatain_dat
import savefiledf2dat as datawritesave 

from hamaker_data import hamaker_calculation  # calculate the hamer constant

# from potential_force import potential_force_algo
from hamaker_calculation import hamaker_save_data
from hamaker_avgvalueeachfile import  save_avg_hamaker
from energy_dissipationEdiss import energy_dissipation

# Enable interactive mode for non-blocking plot display
plt.ion()

# data_path =  "dataproblem\\curvesongold\\"
# data_path =  "dataproblem\\old_data\\"
# data_path =  "dataproblem\\curvesonproteins2\\"  
# data_path = "E:\\python_programs\\xlsfileprocess\\dataproblem\\curves on protein\\with 2000 points\\"
# data_path = "E:\\python_programs\\xlsfileprocess\\dataproblem\\new_data7sep24\\"
data_path = "E:\\Protein-AFM-Analysis-and-Lennard-Jones-potential-fitting\\data\\"

point_density_OLd = 8910.417881801475  # corresponds to avg_windowsize = 4.
avg_windowsize = 4 
# Configure logging
logfilename = "file_process.log"
logfileData_Path = data_path+logfilename
logging.basicConfig(filename=logfileData_Path, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

amp_inOrder,Phase_inOrder = listxlsFiles(data_path)
sameNo_of_amp_phase_length = min(len(amp_inOrder),len(Phase_inOrder))
TotalFiles_processed = 0

filter_saveData = 0  # keep it 1 if you want to save the filtered or smoothed data.

# without_filter_originalsaveData = 1 # keep it 1 if you want to save the without filtered or original raw amp and phase  data.
# ------------ here make either filter_saveData or without_filter_originalsaveData -> 1 not both at the same time as 1. keep 10, 0,1 combination.

# avg_windowsize = calculate_avg_wndsize(data_path,sameNo_of_amp_phase_length,amp_inOrder,Phase_inOrder,point_density_OLd,avg_windowsize)
# print(f"---------------------------------------------------------------------------------------- calculated window size ,4: {avg_windowsize}") 
save_avg_hamakervalues = []   # will save the average hamaker value and corresponding filename of each file and append in this list. 

filename_list = []
hamaker_constavglist = []

for i in range(sameNo_of_amp_phase_length):
    filenameAmplitude = amp_inOrder[i]
    filenamephase = Phase_inOrder[i]
    file_No = i+1     
    print("\n",f"<----- IN process with files {filenameAmplitude} and {filenamephase} and file No. {file_No} -------->")

    print("\n",f"I am dealing with file = {file_No}.")
#     readASdfsetaxisAmpasnp(data_path,filenameAmplitude,filenamephase)
    print(f"I have read and converted the data in dataframe and numpy array and no of row in amp as data_endamp for file {i+1} named as {filenameAmplitude} and {filenamephase}.")
    res = readASdfsetaxisAmpasnp(data_path,filenameAmplitude,filenamephase)
    ampdf = res[0]        # ampdf is two column dataframe with title: ['Piezo','Amplitude'] piezo(um) and Amplitude(nA) 
    phasedf = res[1]      # phasedf is two column dataframe with title: ['Piezo','Phase']
    data_endamp = res[2]   #  total length of ampdf, index of the last value is --> data_endamp-1
    ampdfPiezoColumnarr = res[3]  # it is single column Piezo numpy array  only
    ampdfAmplitudeColumnarr = res[4]    # it is single column  amplitude numpy array only
    A0 = res[5]    # A0 is the last value of the ampdf Amplitude  ***********  check for A0 values if this is in m . I think it is in nA here.

    plt.figure()
    plot_data(ampdf,label='amp',color='blue', marker='', markersize=1,alpha=0.8,title=f"amplitude Vs Piezo {i+1}/{sameNo_of_amp_phase_length}th_data, out of {sameNo_of_amp_phase_length}",Xaxis="Piezo",Yaxis='Amplitude')
    plt.show()
    plt.figure()
    plot_data(phasedf,label='phase',color='red', marker='', markersize=1,alpha=0.6,title=f"Phase Vs Piezo {i+1}/{sameNo_of_amp_phase_length}th_data, out of {sameNo_of_amp_phase_length}",Xaxis="Piezo",Yaxis='Phase')
    # plt.show()
    plt.draw()
    plt.pause(0.1) 
    
    # ------------ *********** here add a function to calculate the avg_window size for each file individually.
    
    avg_windowsize1 = avgws.calculate_avg_wndsize_Individual_filewise(ampdfPiezoColumnarr,file_No,point_density_OLd,avg_windowsize)
    avg_window = avg_windowsize1  # 7,4(more general)  # ******************
        
    list_avg = reverseArrayofAvgValuesWndsize(ampdf,phasedf,avg_window)  # list_avg -> reversed numpy array.
#     plt.figure()
#     plot_data(list_avg,label=f"avg of {avg_window} ",title=f"avg plot of reverse {avg_window} data points for {i+1} file")
#     plt.show()
    
    consecutive_decrease_windowsize = 3   #6,6(3,6 more general)
    index = detect_inflexion_pointAfterAverage(ampdf,list_avg,consecutive_decrease_windowsize) 
    inflexion_After_avg =  index
    print("index of inflexion point w.r.to the average list(i.e. in list_avg) :",inflexion_After_avg,"<-->")
    final_Actual_index = findActualInflexion(inflexion_After_avg,list_avg,data_endamp,avg_window,ampdfAmplitudeColumnarr,ampdfPiezoColumnarr,want_plot=1)
#     final_Actual_index = findActualInflexion(inflexion_After_avg,list_avg,data_endamp,avg_window,ampdfAmplitudeColumnarr,ampdfPiezoColumnarr)
    zero_orFlatAmp = final_Actual_index    #  this the actual index from where we get flat amplitude almost,,after bump Flat region start.
    print(zero_orFlatAmp )
    print(ampdf.iloc[final_Actual_index,0])
    
    # <--------- it is for the finding the downbump in the actual data ... >
    res_indices = smfitbp.findDownBump(ampdf, zero_orFlatAmp, window_length=30, polyorder=3)
    index_inflexion = res_indices[0]
    print("\n index_inflexion ---------->",index_inflexion)
    index_minima = res_indices[1]
    print("\n index_minima ---------->",index_minima)
    smoothed_array = res_indices[4]  # it returned the smoothed array after filtering.
    
    backward_MinimaBump_nmValue = 4.0
    forward_MinimaBump_nmValue = 10.0 
    
#     (ampdata2saveAspiezo_nm,ampdata2saveAsAmplitude_nm,phasedata2savedegree)

    if filter_saveData == 1:
        print(" HERE FILTERED DATA ",end ='->')
        tree(5)
        try: 
            res_m = fitsmoothsave.find1bymcampdfandfit_smmothData(ampdf,phasedf,backward_MinimaBump_nmValue,forward_MinimaBump_nmValue,res_indices,data_endamp,i,zero_orFlatAmp,sameNo_of_amp_phase_length,part2 =None)
    #         res_m = find1bymcampdfandfit(ampdf,phasedf,backward_MinimaBump_nmValue,forward_MinimaBump_nmValue,res_indices,data_endamp,i,zero_orFlatAmp,part2 =None)
            # result_data2save => 
            """ 
            ampdata2saveAspiezo_nm, --------> piezo data in nm from index_inflexion: to dataselect1(zero_orFlatAmp).
            ampdata2saveAsAmplitude_nm, ----> ampdf amplitude data after converting(*1/m) to nm from desired_nmBackIndexwrtoInflexion: to data_choose_endindex(dataendamp)
            phasedata2savedegree, ----------> phase data saved in degree desired_nmBackIndexwrtoInflexion: to data_choose_endindex(dataendamp)
            ampfrominflexion2flat_nm, ------> amplitude from from index_inflexion: to dataselect1(zero_orFlatAmp)
            phasefrominflexion2flat_degree,-> phase from from index_inflexion: to dataselect1(zero_orFlatAmp)
            piezofrominflexion2flat_nm -----> piezo from from index_inflexion: to dataselect1(zero_orFlatAmp)
            m slope in nA/nm  --> do 1/m then become in nm/nA  then can change the ampdf any time from any range to any range.

            """ 
            ampdata2saveAspiezo_nm = res_m[0]           
            ampdata2saveAsAmplitude_nm = res_m[1]
            phasedata2savedegree = res_m[2]
            ampfrominflexion2flat_nm = res_m[3]   # <-- use for hamaker constant 
            phasefrominflexion2flat_degree = res_m[4]  # < -- use for hamaker constant
            piezofrominflexion2flat_nm = res_m[5]   # <--- use for piezo in hamaker constant
            slop_m = res_m[6]  #  do 1/m then become in nm/nA  then can change the ampdf any time from any range to any range
        except Exception as e:
            # Log the error along with the filename
            logging.error(f"Error:occured in function: find1bymcampdfandfit() and loop no:{i+1} and Error occurs in files with names:{filenameAmplitude} and {filenamephase} '{data_path}': {str(e)}")
            continue

    else:
#         if without_filter_originalsaveData == 1:
        print(" HERE RAW DATA UNFILTERED DATA ",end=' ->')
        tree(5)
    # else:
        try:
            res_m = fitsmoothsave.find1bymcampdfandfit(ampdf,phasedf,backward_MinimaBump_nmValue,forward_MinimaBump_nmValue,res_indices,data_endamp,i,zero_orFlatAmp,sameNo_of_amp_phase_length,part2 =None)
            # result_data2save => 
            """ 
            ampdata2saveAspiezo_nm, --------> piezo data in nm from index_inflexion: to dataselect1(zero_orFlatAmp).
            ampdata2saveAsAmplitude_nm, ----> ampdf amplitude data after converting(*1/m) to nm from desired_nmBackIndexwrtoInflexion: to data_choose_endindex(dataendamp)
            phasedata2savedegree, ----------> phase data saved in degree desired_nmBackIndexwrtoInflexion: to data_choose_endindex(dataendamp)
            ampfrominflexion2flat_nm, ------> amplitude from from index_inflexion: to dataselect1(zero_orFlatAmp)
            phasefrominflexion2flat_degree,-> phase from from index_inflexion: to dataselect1(zero_orFlatAmp)
            piezofrominflexion2flat_nm -----> piezo from from index_inflexion: to dataselect1(zero_orFlatAmp)
            m slope in nA/nm  --> do 1/m then become in nm/nA  then can change the ampdf any time from any range to any range.

            """ 
            ampdata2saveAspiezo_nm = res_m[0]
            ampdata2saveAsAmplitude_nm = res_m[1]
            phasedata2savedegree = res_m[2]
            ampfrominflexion2flat_nm = res_m[3]   # <-- use for hamaker constant 
            phasefrominflexion2flat_degree = res_m[4]  # < -- use for hamaker constant
            piezofrominflexion2flat_nm = res_m[5]   # <--- use for piezo in hamaker constant
            slop_m = res_m[6] 
        except Exception as e:
                # Log the error along with the filename
                logging.error(f"Error:occured in function: find1bymcampdfandfit() and loop no:{i+1} and Error occurs in files with names:{filenameAmplitude} and {filenamephase} '{data_path}': {str(e)}")
                continue    
        
        
    
    fdata_path = data_path
    directory_name = "processdata\\"
    directory_path = os.path.join(fdata_path,directory_name)
    if not os.path.exists(directory_path):
        # If not, create the directory
        os.makedirs(directory_path)
        print(f"Directory '{directory_name}' created successfully.")
    else:
        print(f"Directory '{directory_name}' already exists.")

    # here ampdata2saveAspiezo_m is in nm and ampdata2saveAsAmplitude_nm this is also in nm.
    
    filename_res = datawritesave.filesaveDatain_dat(directory_path,ampdata2saveAspiezo_nm,ampdata2saveAsAmplitude_nm,phasedata2savedegree,filenameAmplitude,filenamephase, hamakerConstant = None, A0 = None)
    filename_refinedData = filename_res
    # --------------------------************************************-----------------------------------------------------
    

    datapath = os.path.join(data_path,directory_name)  # datapath where hamker constant data is saved.
    # datapath = "E:\\Protein-AFM-Analysis-and-Lennard-Jones-potential-fitting\\data\\processdata\\"
    # datapath = "E:\python_programs\xlsfileprocess\hamaker_data\hamdata"
    # for filename in os.listdir(datapath):
    print(f"<------here is the filename ---------------->{filename_refinedData}")
    # if filename[-5:] ==".xlsx" and filename[0:7] !='hamaker':
    if filename_refinedData[-4:] ==".dat" and filename_refinedData[0:7] !='hamaker':
        print(f"----------->!!!!!!!! current processing file name is {filename_refinedData} \n") 
#             result = hamaker_const(datapath,filename, hamdeg= None)
#         result = hamaker_calculation.hamaker_const(datapath,filename_refinedData, start_idx=index_inflexion, end_idx =zero_orFlatAmp, hamdeg= None)

#  ------------- set the value of the K,Q,R here -----------------------------
        custom_K = 30.0 # N/m 
        custom_Q = 500
        custom_R = 10  # keep it in nm 
        
        result = hamaker_calculation.hamaker_const(datapath,filename_refinedData, start_idx = index_minima, end_idx = index_minima+25, K=custom_K, Q=custom_Q, R=custom_R, hamdeg= None)

        filename_list.append(result["filename"])
        hamaker_constavglist.append(result["hamaker_const"])

hamaker_constavgData = {"filename":filename_list,"hammaker_constant":hamaker_constavglist }

hamaker_constavgData_df = pd.DataFrame(hamaker_constavgData)

hamaker_constavgData_df.to_excel(os.path.join(datapath,'hamaker_avgValeachfile.xlsx'))        

    
       
    
"""
    #  filename_res  from return (filename,filenamehawmaker) 

#     filesaveDatain_dat(directory_path,piezofrominflexion2flat_nm,ampfrominflexion2flat_nm ,phasefrominflexion2flat_degree,filenameAmplitude,filenamephase,hamakerConstant = 1,A0 = A0)
    
#     print("\n",f"<--------------- process is completed with files {filenameAmplitude} and {filenamephase} and file sequence No. {i+1}.------------------------------>")
    
#     potential_force_algo(directory_path,filename_res) 
# K=32.125 Q=442
    ampdata2saveAsAmplitude_converted2meter = ampdata2saveAsAmplitude_nm * 1e-9  # last value in ampdf converted to m  
    # Access the last value and assign to A0_hamaker
    A0_hamaker = ampdata2saveAsAmplitude_converted2meter.iloc[-1] 
    
    # hamaker_save_data(data_path, ampfrominflexion2flat_nm, phasefrominflexion2flat_degree, piezofrominflexion2flat_nm, filenameAmplitude, filenamephase, A0 = A0_hamaker, K = 26.98, Q = 466, R =10 * 10E-9)  # A0 = A0_hamaker(meter).  # this will calculate hamaker from inflexion(just before bump) to zero_flatAmp 

    res_hamaker = hamaker_save_data(data_path, ampfrominflexion2flat_nm, phasedata2savedegree, ampdata2saveAspiezo_nm, filenameAmplitude, filenamephase, A0 = A0_hamaker, K = 26.98, Q = 466, R =10 * 10E-9)  # A0 = A0_hamaker(meter). # hamaker constant from inflexion to end of dataframe (endAmp) 
    # these nm value of amp,phase and piezo changed in the meter inside the hamaker_save_data() function.
    # save_avg_hamaker(data_path, res_hamaker[0], res_hamaker[1], output_filename ='all_avg_hamaker.xlsx')  # average_hamaker values for each file --> res_hamker[1] , this is hamaker file name --> res_hamaker[0]
    print(f"<<<<<<<<<<<<<<<<_____*********************************************************** {res_hamaker[0]} <----------------> {res_hamaker[1]}")
    save_avg_hamakervalues.append((res_hamaker[0], res_hamaker[1]))

    TotalFiles_processed = TotalFiles_processed + 1
    print(f"<--! file saved and hawmaker constant caluclation processed file no out of:{TotalFiles_processed}/{sameNo_of_amp_phase_length}  ! ---------------->")
    
    # energy_dissipation(data_path, ampfrominflexion2flat_nm, phasefrominflexion2flat_degree, piezofrominflexion2flat_nm, filenameAmplitude, filenamephase, A0, K = 2.56, Q = 234)  # energy dessipation from inflexion(just before bump) to zero_flatAmp.
    
    #  ampdf_energy = ampdfAmplitudeColumnarr*(1e-9/slop_m)  # m 
    # phasedf
    # ampdf
    energy_dissipation(data_path, ampdata2saveAsAmplitude_nm, phasedata2savedegree, ampdata2saveAspiezo_nm, filenameAmplitude, filenamephase, A0 = A0_hamaker, K = 26.98, Q = 466)  # energy dessipation from inflexion to end of dataframe (endAmp) 
    
    print(f"<--! file saved and energy dissipation is done and processed file no out of:{TotalFiles_processed}/{sameNo_of_amp_phase_length}  ! ---------------->")
# save the average_hamaker values in the file from the save_avg_hamakervalues list.  
save_avg_hamaker(data_path,save_avg_hamakervalues,output_filename="avg_hamaker_results.xlsx")  
"""