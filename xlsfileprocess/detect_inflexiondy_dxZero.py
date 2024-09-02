
""" 
list_avg --> it is the list of average values of window size(= avg_window)
ampdf --> dataFrame extracted from the Amplitude excel files and set_index as Piezo for x and 'Amplitude' for y .
phasedf --> dataFrame extracted from the pahse excel files and set_index as Piezo for x and 'Phase' for y .
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def detect_inflexion_pointAfterAverage(ampdf,list_avg, consecutive_decrease_windowsize):
    ampdfAmplitudeColumn = np.array(ampdf['Amplitude'])
    # rows = ampdfAmplitudeColumn.shape[0]
    # flipampdfAmplitudeColumn = np.flip(ampdfAmplitudeColumn)
    # values  = ampdfAmplitudeColumn   # it is list or numpy array.
    # ampdfPiezoColumn = np.array(ampdf['Piezo'])
    # print(list_avg)  # <- 
    consecutive_decreases = consecutive_decrease_windowsize
#    
    num_decreases = 0
    inflexion_indexofAveragedAmplitude = None

    for i in range(1, len(list_avg)):
        # print("just entered inside the for loop",i)
        if list_avg[i] < list_avg[i-1]:  # Check if the current value is less than the previous one
            num_decreases += 1
            # print("modified check",num_decreases)
            # if num_decreases >= consecutive_decreases and (abs(list_avg[i] - list_avg[i-consecutive_decreases]) >= 0.0625125):
            if num_decreases >= consecutive_decreases and (abs(list_avg[i] - list_avg[i-consecutive_decreases]) >= 0.125):
            # if num_decreases >= consecutive_decreases:
                print("<------------------------!!!!----------------------------->",list_avg[i],list_avg[i-consecutive_decreases-1])
                inflexion_indexofAveragedAmplitude = i - consecutive_decreases + 1   # (<- it should be 1 less, index start from zero in actual.)
#                 inflexion_index = i - consecutive_decreases + 1
                # inflexion_indexofAveragedAmplitude = i - consecutive_decreases    # (<- it should be 1 less, index start from zero in actual.)
                
                break
        else:
            num_decreases = 0  # Reset the count 
    try:
        return inflexion_indexofAveragedAmplitude
    except :
        print("check the average window size :")
    finally:    
         print(f"please Reduce Average window size i.e. avg_window, keep it less than 10, if you get index = None")
    


if __name__=="__main__":
    excel_path = "E:\\python_programs\\xlsfileprocess\\dataproblem\\"
    filenameAmplitude = 'Amplitude28.xlsx'
    ampdf = pd.read_excel(excel_path+filenameAmplitude)
    ampdf= ampdf.set_axis(['Piezo','Amplitude'],axis='columns')
    print(ampdf.head(),"\n")
    filenamephase = 'phase28.xlsx'
    phasedf = pd.read_excel(excel_path+filenamephase)
    phasedf=phasedf.set_axis(['Piezo','Amplitude'],axis='columns')
    print(phasedf.head(),"\n")
    print(ampdf.shape)
    # x= nm,  y= nA
    data_endamp =ampdf.shape[0]
    print("end dat pints = \n",data_endamp)
    consecutive_decrease_windowsize = 8
    from reverseArrayOfAvgWindow import reverseArrayofAvgValuesWndsize
    # avg_window = 10
    list_avg = reverseArrayofAvgValuesWndsize(ampdf,phasedf,consecutive_decrease_windowsize)

    index = detect_inflexion_pointAfterAverage(ampdf,list_avg,consecutive_decrease_windowsize)
    print("index = ",index)
    a =index
    # b=rows
    # print("a:",a,"b:",b)




