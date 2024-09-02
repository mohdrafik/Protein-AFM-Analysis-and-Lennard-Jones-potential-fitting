import matplotlib.pyplot as plt
def findActualInflexion(inflexion_After_avg,list_avg,data_endamp,avg_window,ampdfAmplitudeColumnarr,ampdfPiezoColumnarr,want_plot=None):

    inflexion_index_afterAverage   = inflexion_After_avg
    y_scatter_indexforavg = list_avg[inflexion_index_afterAverage]
    print("Inflexion index:", inflexion_index_afterAverage)
    plt.plot(list_avg)
    plt.scatter(inflexion_index_afterAverage,y_scatter_indexforavg)
    plt.grid()
    plt.ylim([7,9.2])
    plt.show()


    # below I will calculate the actual inflexion point with the original index of the ampdf.
    # <---------------- now Calculate the original index for that resversed Array and then conver back that point in Straight array also ----> 
    inflexion_index_afterAverage_startZero =  inflexion_index_afterAverage-1
    index_Actual_reverseArray = ((inflexion_index_afterAverage_startZero+ 1)* avg_window) - avg_window + 1 
    last_index_ampdf = data_endamp # ampdfAmplitudeColumn.shape # <-- num of rows
    # print("size of the ampdf[\"Amplitude\"] ", ampdfAmplitudeColumn.shape)
    index_Actual_Array = last_index_ampdf - index_Actual_reverseArray + 1
    final_Actual_index =  index_Actual_Array -1

    print(" this the actual index from where we get flat amplitude almost ! --> ",final_Actual_index)  # 

    # main plot and inflexion point w.r.to main data 
    y_actual = ampdfAmplitudeColumnarr[final_Actual_index]
    x_scatter = ampdfPiezoColumnarr[final_Actual_index] 
    # plt.figure
    if want_plot == None:
        pass
    else:
        plt.plot(ampdfPiezoColumnarr,ampdfAmplitudeColumnarr,'-r',alpha=0.2)
        plt.scatter(x_scatter,y_actual,marker ='<',s=150,alpha=0.8,label='Data(nm)')
        plt.title(" it is final ")
        plt.grid()
        plt.show()

    return final_Actual_index 