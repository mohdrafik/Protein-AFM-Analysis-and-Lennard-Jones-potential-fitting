"""
here in arguments we will always try to give the  dataframe like ampdf and phasedf 
ampdf (as a dataframe given to the function) --> ampdf   = pd.read_excel(comp_datapathAmp)  
phasedf (as a dataframe given to the function) --> phasedf = pd.read_excel(comp_datapathPhase)
"""
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt

def reverseArrayofAvgValuesWndsize(ampdf,phasedf,avg_window):
    # ampdf = ampdf.set_axis(['Piezo','Amplitude'], axis ='columns')
    # phasedf = phasedf.set_axis(['Piezo','Phase'], axis ='columns')
    # print("\n",phasedf.head(),"\n",phasedf.shape,"\n")
    #  < ----------- Above changed the column name(set index) from x,y to Piezo, Amplitude and Phase 
    ampdfAmplitudeColumn = np.array(ampdf['Amplitude'])    # convert to numpy array
    ampdfPiezoColumn = np.array(ampdf['Piezo'])   # convert to numpy array
    
    reversed_ampdfAmplitudeColumn = np.flipud(ampdfAmplitudeColumn)
    x = ampdfPiezoColumn
    y = reversed_ampdfAmplitudeColumn
    
    rows_ampdfAmp = y.shape[0]  # give size of the ampdf.
    # avg_window = 10 
    list_avg_windowSize = []
    count_window = 0
    list_avg = []
    count_listavgEntry = 0
    

    for val in y:
        count_window = count_window + 1
        list_avg_windowSize.append(val)
    #     print(list_avg_windowSize,end=' ') 
        if len(list_avg_windowSize) == avg_window:
    #         print(list_avg_windowSize)
            count_listavgEntry += 1
            avg_ofwindowsizeElements = sum(list_avg_windowSize)/avg_window
    #         print(avg_ofwindowsizeElements,end =' ,')
            list_avg.append(avg_ofwindowsizeElements)
            
            list_avg_windowSize = []   # here list is reset
    #         print(" to check the size of the is it reset or not -->!!!",len(list_avg_windowSize))
            
    # plt.plot(list_avg)
    # plt.show()
    return list_avg
# if __name__=="__main__":
#     path =
        

    