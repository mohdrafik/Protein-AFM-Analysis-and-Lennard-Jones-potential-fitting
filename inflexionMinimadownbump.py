import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import savgol_filter


def findDownBump(ampdf, zero_orFlatAmp, window_length= None, polyorder=None):
    """
          "\n Actual inflexion point Index with original data: ", result[0],
          "\n Actual Minima point Index before Slicing with original Data: ", result[1],
          "\n Inflexion point index after slicing: ", result[2],
          "\n smoothed array of same size as input in the filter here just see the size: ", result[4].shape,
          "\n Minima point Index After slicing: ", result[3])
     -->  Apply Savitzky-Golay filter for smoothing
    
    """
    ampdfAmplitudeColumn = np.array(ampdf['Amplitude'])
    slicingStartIndex = 4
    ampdfAmplitudeColumn = ampdfAmplitudeColumn[slicingStartIndex:zero_orFlatAmp]
    y1 = ampdfAmplitudeColumn
    # Smoothing the data
    smoothed_amp = savgol_filter(ampdfAmplitudeColumn, window_length, polyorder)

    print("The shape and size of the amplitude array before the np.diff: (4:data endpoint)\n", ampdfAmplitudeColumn.shape)
    y = smoothed_amp

    x = ampdf['Piezo'][slicingStartIndex:zero_orFlatAmp]
    print("x values\n and shape of x ", x[0:5], x.shape)
    x = np.array(x)
    arr = np.diff(smoothed_amp)

    print("I am inside the array: function array\n:", arr[0:10])
    neg_indices = np.where(arr < 0)[0]  # Find where the array is negative

    if len(neg_indices) == 0:  # If there are no negative values, return an empty array
        return np.array([])

    # Identify all generally decreasing sequences
    sequences = []
    current_sequence = [neg_indices[0]]
    for i in range(1, len(neg_indices)):
        if neg_indices[i] == neg_indices[i-1] + 1 or smoothed_amp[neg_indices[i]] <= smoothed_amp[neg_indices[i-1]]:
            current_sequence.append(neg_indices[i])
        else:
            sequences.append(current_sequence)
            current_sequence = [neg_indices[i]]
    sequences.append(current_sequence)

    # Calculate the magnitude of decrease for each sequence
    magnitudes = [smoothed_amp[seq[0]] - smoothed_amp[seq[-1]] for seq in sequences]

    # Find the sequence with the highest downward magnitude
    max_magnitude_index = np.argmax(magnitudes)
    longest_sequence = sequences[max_magnitude_index]

    print("longest sequence =\n", longest_sequence)  # Longest consecutive negative going sequence index value we get here
    print("x axis=\n", x[longest_sequence])

    print("scat val x: \t \n", longest_sequence[0])

    xscat = x[longest_sequence[0]]  # It returns the index values for the minima starting points array

    print("scat val y: \t \n", arr[longest_sequence][0])
    yscat = y[longest_sequence[0]]
    # Plotting --------------------------------------------------------------------------->
    plt.plot(x, y1, '.m')

    #     plt.plot(x,y,'.b')
    plt.scatter(xscat, yscat, color='red', marker='o', s=150, label='Decreasing Points')  # s=100, marker='o'
    plt.scatter(x[longest_sequence[-1] + 1], y[longest_sequence[-1] + 1], s=150, color='red', marker='*', label='Minima point')
    plt.xlabel('Piezo')
    plt.ylabel('Amplitude')
    plt.title('Circle: inflexion point, Star: Minima Point ')
    plt.grid()

    plt.show()

    plt.close()

    # Plotting --------------------------------------------------------------------------->
    plt.subplot(2, 1, 1)
    plt.plot(x, ampdfAmplitudeColumn,'.-', color='blue', markersize=2, linewidth=0.5, alpha=0.3, label='Original Data')
    plt.plot(x, smoothed_amp, '-r', label='Smoothed Data')
    plt.xlabel('Piezo')
    plt.ylabel('Amplitude')
    plt.title('Original vs Smoothed Data')
    plt.legend()
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.plot(x, y, '.-', color='gray', markersize=2, linewidth=0.5, alpha=0.3, label='Smoothed Data')       #'.-', color='gray', markersize=2, linewidth=0.5, alpha=0.3,
    plt.scatter(xscat, yscat, color='red', marker='o', s=100, label='Decreasing Points')                    # s=100, marker='o'
    plt.scatter(x[longest_sequence[-1] + 1], y[longest_sequence[-1] + 1], s=90, color='red', marker='*', label='Minima Point')
    plt.xlabel('Piezo')
    plt.ylabel('Amplitude')
    plt.title('Circle: Inflexion Point, Star: Minima Point')
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()

    ActualInflexionPointActualRawDataIndex = longest_sequence[0] + slicingStartIndex
    ActualMinimaPointActualRawDataIndex = longest_sequence[-1] + slicingStartIndex + 1
    # ActualMinimaPointActualRawDataIndex = longest_sequence[-1] + slicingStartIndex     # improved without 1

    InflexionAfterSliceIndex = longest_sequence[0]
    MinimaPointAfterSliceIndex = longest_sequence[-1] + 1
    # MinimaPointAfterSliceIndex = longest_sequence[-1]     # improved without 1

    result = (ActualInflexionPointActualRawDataIndex, ActualMinimaPointActualRawDataIndex, InflexionAfterSliceIndex, MinimaPointAfterSliceIndex,smoothed_amp)
    print("\n Actual inflexion point Index with original data: ", result[0],
          "\n Actual Minima point Index before Slicing with original Data: ", result[1],
          "\n Inflexion point index after slicing: ", result[2],
          "\n smoothed array of same size as input in the filter here just see the size: ", result[4].shape,
          "\n Minima point Index After slicing: ", result[3])

    return result
# < ----------------------------------------- BELOW ANOTHER OLD FUNCTION Without smoothening --------------------------------------------------------------------->

def findDownBump_old(ampdf, zero_orFlatAmp):
    
    ampdfAmplitudeColumn = np.array(ampdf['Amplitude'])
    slicingStartIndex = 4
    ampdfAmplitudeColumn = ampdfAmplitudeColumn[slicingStartIndex:zero_orFlatAmp]
    print(" the shape and size of the amplitude array before the np.diff: (4:dataendpoint) \n",ampdfAmplitudeColumn.shape)
    y = ampdfAmplitudeColumn

    x = ampdf['Piezo'][slicingStartIndex:zero_orFlatAmp]
    print("x values\n and shape of x ",x[0:5], x.shape)
    x = np.array(x)
    arr =  np.diff(ampdfAmplitudeColumn)

    print("I am indside the array: function arary \n:",arr[0:10])
    neg_indices = np.where(arr < 0)[0]  # Find where the array is negative

     
    if len(neg_indices) == 0:    # If there are no negative values, return an empty array
        return np.array([])

    # Find the consecutive differences of indices
    diff = np.diff(neg_indices)

    # Find where the differences are not equal to 1
    diff_not_1 = np.where(diff != 1)[0]

    split_indices = np.split(neg_indices, diff_not_1 + 1)  # Split the indices into consecutive sequences

    lengths = np.array([len(seq) for seq in split_indices])     # Find the length of each consecutive sequence
    max_length_index = np.argmax(lengths)      # Find the index of the longest consecutive sequence

    longest_sequence = split_indices[max_length_index]   # Get the longest consecutive sequence

    print("longest sequence =\n",longest_sequence)  #longest consecutive negative going sequence index value we get here
    # x = list(range(len(arr)))
    print("x axis=\n",x[longest_sequence])

    print("scat val x: \t \n",longest_sequence[0])

    # xscat = longest_sequence[0]    
    xscat  = x[longest_sequence[0]]   # it returns the index values for the minima starting points array

    print("scat val y: \t \n",arr[longest_sequence][0])
    # yscat = arr[[longest_sequence][0]]

    yscat = y[longest_sequence[0]]

    plt.plot(x,y,'.b')
    plt.scatter(xscat,yscat,color='red',marker= 'o',s = 100 ,label='Decreasing Points') # s=100, marker='o'
    plt.scatter(x[longest_sequence[-1]+1 ],y[longest_sequence[-1] +1],s = 90,color='red',marker= '*',label='Decreasing Points')  
    plt.xlabel('Piezo')
    plt.ylabel('Amplitude')
    plt.title('Circle:inflexion point, Star: Minima Point ')
    plt.grid()

    plt.show() 

    plt.close()

    ActualInflexionPointActualRawDataIndex = longest_sequence[0] + slicingStartIndex
    ActualMinimaPointActualRawDataIndex  = longest_sequence[-1] + slicingStartIndex + 1
    
    InflexionAfterSliceIndex = longest_sequence[0] 
    MinimaPointAfterSliceIndex  = longest_sequence[-1] +  1
    # plt.show()

    result = (ActualInflexionPointActualRawDataIndex , ActualMinimaPointActualRawDataIndex, InflexionAfterSliceIndex, MinimaPointAfterSliceIndex)
    print("\n Actual inflexion point Index with original data :  ", result[0],
          " \n Actual Minima point Index before Slicing with original Data : ", result[1],
            "\n inflexion point index after slicing: ", result[2],
        "\n Minima point Index After slicing: ",result[3])


    return (ActualInflexionPointActualRawDataIndex , ActualMinimaPointActualRawDataIndex, InflexionAfterSliceIndex, MinimaPointAfterSliceIndex)
    


if __name__ == "__main__":
    
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import scipy.io as sio
    import os
    from termcolor import colored
    import logging

    from listxlsfilesinOrder import listxlsFiles
    from converdfSetAxisgetNumpyArray import readASdfsetaxisAmpasnp
    from plotmatlabfun import plot_data
    from reverseArrayOfAvgWindow import reverseArrayofAvgValuesWndsize
    from detect_inflexiondy_dxZero import detect_inflexion_pointAfterAverage
    from final_index_calculation import findActualInflexion
    import average_windowsize as avgws 

#     data_path = "E:\\python_programs\\xlsfileprocess\\dataproblem\\curves on protein\\with 2000 points\\"
    data_path = "E:\\python_programs\\xlsfileprocess\\dataproblem\\test_data\\"

    point_density_OLd = 8910.417881801475  # corresponds to avg_windowsize = 4.
    avg_windowsize = 4
    # Configure logging
    logfilename = "file_process.log"
    logfileData_Path = data_path + logfilename
    logging.basicConfig(filename=logfileData_Path, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    amp_inOrder, Phase_inOrder = listxlsFiles(data_path)
    sameNo_of_amp_phase_length = min(len(amp_inOrder), len(Phase_inOrder))
    TotalFiles_processed = 0

#     avg_windowsize = calculate_avg_wndsize(data_path, sameNo_of_amp_phase_length, amp_inOrder, Phase_inOrder, point_density_OLd, avg_windowsize)
#     print(f"---------------------------------------------------------------------------------------- calculated window size ,4: {avg_windowsize}")

    for i in range(sameNo_of_amp_phase_length):
        filenameAmplitude = amp_inOrder[i]
        filenamephase = Phase_inOrder[i]
        file_No = i + 1
        print("\n", f"<----- IN process with files {filenameAmplitude} and {filenamephase} and file No. {file_No} -------->")

        print("\n", f"I am dealing with file = {file_No}.")
        print(f"I have read and converted the data in dataframe and numpy array and no of row in amp as data_endamp for file {i + 1} named as {filenameAmplitude} and {filenamephase}.")
        res = readASdfsetaxisAmpasnp(data_path, filenameAmplitude, filenamephase)
        ampdf = res[0]  # ampdf is two column dataframe with title: ['Piezo','Amplitude']
        phasedf = res[1]  # phasedf is two column dataframe with title: ['Piezo','Phase']
        data_endamp = res[2]  # total length of ampdf, index of the last value is --> data_endamp-1
        ampdfPiezoColumnarr = res[3]  # it is single column Piezo numpy array only
        ampdfAmplitudeColumnarr = res[4]  # it is single column amplitude numpy array only
        A0 = res[5]  # A0 is the last value of the ampdf Amplitude

        avg_windowsize1 = avgws.calculate_avg_wndsize_Individual_filewise(ampdfPiezoColumnarr,file_No,point_density_OLd,avg_windowsize)
        
        avg_window = avg_windowsize1  # 7,4(more general)  # ******************
        list_avg = reverseArrayofAvgValuesWndsize(ampdf, phasedf, avg_window)  # list_avg -> reversed numpy array.
#         plt.figure()
#         plot_data(list_avg, label=f"avg of {avg_window} ", title=f"avg plot of reverse {avg_window} data points for {i}")
#         plt.show()
        
        consecutive_decrease_windowsize = 3   #6,6(more general)
        index = detect_inflexion_pointAfterAverage(ampdf,list_avg,consecutive_decrease_windowsize) 
        inflexion_After_avg =  index
        print("index of inflexion point w.r.to the average list(i.e. in list_avg) :",inflexion_After_avg,"and Avg window:",avg_window)
        plt.figure()
        plot_data(list_avg, label=f"avg of {avg_window} ", title=f"avg plot of reverse {avg_window} data points for {i}")
        plt.scatter(inflexion_After_avg,list_avg[inflexion_After_avg],color='red', marker='o', s=100, label='Inflexion')
        plt.show()
            
            
        final_Actual_index = findActualInflexion(inflexion_After_avg,list_avg,data_endamp,avg_window,ampdfAmplitudeColumnarr,ampdfPiezoColumnarr,want_plot=None)
#         final_Actual_index = findActualInflexion(inflexion_After_avg,list_avg,data_endamp,avg_window,ampdfAmplitudeColumnarr,ampdfPiezoColumnarr)
        zero_orFlatAmp = final_Actual_index
        print(zero_orFlatAmp )
        print(ampdf.iloc[final_Actual_index,0])

        res_downbump = findDownBump(ampdf, zero_orFlatAmp, window_length=30, polyorder=3)
    

