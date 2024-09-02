import pandas as pd
import numpy as np 
def readASdfsetaxisAmpasnp(data_path,filenameAmplitude,filenamephase): 

    # from inflexionMinimadownbump import findDownBump 
    # excel_path = "C:\\Users\\mrafik\\Desktop\\python_general_code\\xlsfileprocess\\"
#     excel_path = "E:\\python_programs\\xlsfileprocess\\dataproblem\\"
    # excel_path = "E:\\python_programs\\xlsfileprocess\\"
    excel_path = data_path
#     filenameAmplitude = 'Amplitude40.xlsx'
    ampdf = pd.read_excel(excel_path+filenameAmplitude)
    ampdf = ampdf.set_axis(['Piezo','Amplitude'],axis='columns')
    if ampdf['Piezo'].iloc[0] > ampdf['Piezo'].iloc[-1]:  # if  piezo value is start from higher(+ve) to lower(-ve)
        ampdf = ampdf.loc[::-1].reset_index(drop=True)

    print(ampdf.head(),"\n")
    #  ------------------------- phase -------------------- > 
#     filenamephase = 'phase40.xlsx' 
    phasedf = pd.read_excel(excel_path+filenamephase)
    phasedf = phasedf.set_axis(['Piezo','Phase'],axis='columns')
    if phasedf['Piezo'].iloc[0] > phasedf['Piezo'].iloc[-1]:
        phasedf = phasedf.loc[::-1].reset_index(drop=True)
        
    print(phasedf.head(),"\n")
    print(ampdf.shape)
    # x= nm  , y= nA
    # <--------------------------- these two points are used later data_endamp and ampdfPiezoColumn --------->
    data_endamp = ampdf.shape[0]
    print("end data points = \n",data_endamp)
    A0 = ampdf['Amplitude'][data_endamp-1]           # A0 is the last value of the ampdf
    ampdfPiezoColumnarr = np.array(ampdf['Piezo'])  # name chnaged to ampdfPiezoColumn from to ampdfPiezoColumnarr

    ampdfAmplitudeColumnarr = np.array(ampdf['Amplitude'])
    
    return  (ampdf,phasedf,data_endamp,ampdfPiezoColumnarr,ampdfAmplitudeColumnarr,A0) 
