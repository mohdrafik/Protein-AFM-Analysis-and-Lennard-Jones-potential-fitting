# backward_MinimaBump_nmValue = 4.0
# forward_MinimaBump_nmValue = 10.0

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import savgol_filter

def find1bymcampdfandfit_smmothData(ampdf,phasedf,backward_MinimaBump_nmValue,forward_MinimaBump_nmValue,res_indices,data_endamp,i,zero_orFlatAmp,sameNo_of_amp_phase_length,part2 = None):
    
    ampdf_array = np.array(ampdf['Amplitude'])
    ampdf_amplitude_filtered = savgol_filter(ampdf_array, window_length=30, polyorder=3)
    # Ensure both arrays have the same length
    assert len(ampdf_amplitude_filtered) == len(ampdf['Piezo']), "The length of amparray and piezo_series must be the same."
    # Create again new "ampdf" DataFrame with filtered amplitude values
    ampdf = pd.DataFrame({
        'Piezo': ampdf['Piezo'],
        'Amplitude': ampdf_amplitude_filtered
    })

    #************************** this  is for phase filtering if we need in future we will use this.   
    phasedf_phase_filtered = savgol_filter(phasedf['Phase'], window_length=20, polyorder=3)
    assert len(phasedf_phase_filtered) == len(phasedf['Piezo']), "The length of phase and piezo_series must be the same."
    # Create again new "ampdf" DataFrame with filtered amplitude values
    phasedf = pd.DataFrame({
        'Piezo': phasedf['Piezo'],
        'Phase': phasedf_phase_filtered
    })



    xpiezo_nm = 1000*ampdf['Piezo']  # now xpiezo_nm in nm --> after multiplying by 1000 become in nm earlier ampdf['Piezo'] was in micro meter.
    x_diff = np.diff(ampdf['Piezo'])
    d_nm = 1000*x_diff[5]   # this is in nanometer (nm) now. 
    dataselect1 = zero_orFlatAmp
    # print("d in nm \t:",d_nm)
    # count = 0
    # for val in x_diff:
    #     # just to check common differences between piezo values.
    #     count = count+1
    #     print(val)
    #     if count ==5:
    #         break
            
    # plt.plot(list(range(len(x_diff))), ampdf['Piezo'])    
    # plt.show()
    # #     print()

    # here 2.5,3nm any value we put get corresponding N 
    # backward_MinimaBump_nmValue = 4.0  # <------------- make it as argument in func.
    N_count_back = (backward_MinimaBump_nmValue)/(d_nm)  # (using a+(n-1)D)

    N_count_back = np.ceil(N_count_back)
    print("n count back = ",N_count_back)

    desired_nmBackIndexwrtoInflexion = res_indices[0] - N_count_back  # it is from the inflexion point index_inflexion = index_inflexion - 4 
    # it has been seen in the results, index is shifted towards right,to compensate it just pull it left side.
    desired_nmBackIndexwrtoMinima = res_indices[1] - N_count_back  # this is from the minima point
    # desired_nmBackIndex
    # now time to choose the data 3nm after the minima(bump):
    # forward_MinimaBump_nmValue = 10.0     # <------------- make it as argument in func.
    
    N_count_forward = (forward_MinimaBump_nmValue)/(d_nm)  # (using a+(n-1)D)
    N_count_forward = np.ceil(N_count_forward)
    data_choose_endindex = res_indices[1] + int(N_count_forward)
    data_choose_endindex = data_endamp


    desired_nmBackIndexwrtoInflexion = int(desired_nmBackIndexwrtoInflexion)
    if desired_nmBackIndexwrtoInflexion < 0:
        desired_nmBackIndexwrtoInflexion = 0
    desired_nmBackIndexwrtoMinima = int(desired_nmBackIndexwrtoMinima)
    if desired_nmBackIndexwrtoMinima < 0:
        desired_nmBackIndexwrtoMinima = 0

    print("\n index starting wrto inflexion : ",desired_nmBackIndexwrtoInflexion, 
        "\n index starting wrto Minima : ",desired_nmBackIndexwrtoMinima)




    ##### ----------this is for linear fitting the data from desired point to the inflexion points data :-----------##
    # Perform linear regression for linear fitting
    index_inflexion = res_indices[0]   # < -- it is inflexion point 
    index_inflexion_new = index_inflexion - 4    # here as i have seen that inflexion index should be bit less than that we got, reduced by 4 index.
    ampdf_x_nm = 1000*ampdf['Piezo'][desired_nmBackIndexwrtoInflexion:index_inflexion_new]
    ampdf_y_nA = ampdf['Amplitude'][desired_nmBackIndexwrtoInflexion:index_inflexion_new]

    coefficients = np.polyfit(ampdf_x_nm,ampdf_y_nA, 1)

    m, c = coefficients
    # Print the results
    print(f"m (slope in nA/nm ): for {i+1} file data {m}")
    print(f"c, zero intercept nA (intercept): for {i+1} file data {c}")

    ampdf_y_nm = (1/m)*ampdf_y_nA    #--------****** save this data as Amplitude in .dat file----------*********** 

    poly = np.poly1d(coefficients)  # this is like f(x) = m*x + c , give x values get y values.

    # Plot the data and the linear fit
    fig, ax1 = plt.subplots()
    ax1.plot(ampdf_x_nm,ampdf_y_nm, marker ='.',label='Data(nm)')
    ax1.set_xlabel('piezo(nm)')  
    ax1.set_ylabel('Amplitude(nm)',color='b')
    ax1.tick_params('y', colors='b')  # this will make blue color font on y axis left side.
    ax1.grid()
    ax1.legend()

    ax2= ax1.twinx()  # it will share the x axis --> twinx()
    ax2.plot(ampdf_x_nm, ampdf_y_nA, color='green',marker ='.',label='Data(nA)')
    ax2.plot(ampdf_x_nm, poly(ampdf_x_nm), color='red', label='Linear Fit') 
    ax2.set_xlabel('piezo(nm)')
    ax2.set_ylabel('Amplitude(nA)',color='r')
    ax2.tick_params('y',colors = 'r')
    ax2.set_ylim([6,10])
    # ax2.set_grid()
    ax2.legend(loc=[0.02,0.79])
    plt.title('Linear fitting of the ampltitude and piezo data')
    plt.show()


    # ************ ------------ this is working fine for me ----------------------******************
    # same data but another figure 

    fig
    plt.scatter(ampdf_x_nm, ampdf_y_nA, marker ='.',label='Data(nA)')

    plt.scatter(ampdf_x_nm,ampdf_y_nm, marker ='*',label='Data(nm)') # THIS IS FOR CONVERTED Y DATA TO nm --> y=  y*(1/m)

    plt.plot(ampdf_x_nm, poly(ampdf_x_nm), color='red', label='Linear Fit')

    plt.grid()
    plt.xlabel('piezo(nm)')
    plt.ylabel('Amplitude(nA)')
    plt.title('Linear fitting of the ampltitude and piezo data')
    plt.legend()
    plt.show()


    # ----------------******************************* this is the final data we will save in .dat file .------------------
    ampdata2saveAspiezo_nm = xpiezo_nm[desired_nmBackIndexwrtoInflexion:data_choose_endindex]   # data_choose_endindex --> it is the last index = dataendamp 979 
    print(ampdata2saveAspiezo_nm.head())
    # ampdata2saveAspiezo_nm = ampdata2saveAspiezo_nm + c/m
    ampdata2saveAspiezo_nm = ampdata2saveAspiezo_nm - ampdata2saveAspiezo_nm[desired_nmBackIndexwrtoInflexion] 

    ampdata2saveAsAmplitude_nm = (1/m)* ampdf['Amplitude'][desired_nmBackIndexwrtoInflexion:data_choose_endindex]

    ampdata2saveAsAmplitude_nm.shape
    plt.plot(ampdata2saveAspiezo_nm,ampdata2saveAsAmplitude_nm,'-r')
    plt.grid()
    plt.xlabel('piezo(nm)')
    plt.ylabel('Amplitude(nm)')
    plt.title(f"just to check before saving to .dat file no. no.{i+1}/{sameNo_of_amp_phase_length}")
    # plt.legend()
    plt.show()


    # #  this is for the phase values:---------------------------------********


    print(phasedf.iloc[0,1]) # first value added -- phasedf.iloc[0,1]
    # last value add ---- > phasedf.iloc[data_endamp-1,1] 

    phase  = - phasedf['Phase'] -90 + phasedf.iloc[data_endamp-1,1]
    print("\n", phase.shape)
    print("\n new phase values: \n", phase[0:5])

    phasedata2savedegree = phase[desired_nmBackIndexwrtoInflexion:data_choose_endindex]

    plt.plot(ampdata2saveAspiezo_nm,phasedata2savedegree,'-b')
    plt.grid()
    plt.xlabel('piezo(nm)')
    plt.ylabel('phase(o)')
    plt.title(f"PHASE in degree just to check before saving to .dat file no.{i+1}/{sameNo_of_amp_phase_length}")
    # plt.legend()
    plt.show()

# <----------------------------any data can select depend on the starting and ending points given in arguments or defined above. ---------------- >
    # <------------------ use these two as base and select any data part from this here phase in degree and ampdf in nm. ------------- >
    # ampdata2saveAsAmplitude_nm = (1/m)* ampdf['Amplitude']    # <---- in nm  
    # phasedata2savedegree = phase                              # <----- in degree 
    
    ampfrominflexion2flat_nm = (1/m)* ampdf['Amplitude'][index_inflexion:dataselect1]  # dataselect1 = zero_orFlatAmp
    phasefrominflexion2flat_degree = phase[index_inflexion:dataselect1]                #  dataselect1 = zero_orFlatAmp
    piezofrominflexion2flat_nm  = ampdata2saveAspiezo_nm[index_inflexion:dataselect1]   # <--- this is the final data to save as piezo in nm.

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

    # # now generate a .dat file from the where data is saved ( unit: nm)
    return (ampdata2saveAspiezo_nm,ampdata2saveAsAmplitude_nm,phasedata2savedegree,ampfrominflexion2flat_nm,phasefrominflexion2flat_degree,piezofrominflexion2flat_nm,m)



# ***************************************** Below given function, that works for the ampdf original data without fitting. *****************************************

def find1bymcampdfandfit(ampdf,phasedf,backward_MinimaBump_nmValue,forward_MinimaBump_nmValue,res_indices,data_endamp,i,zero_orFlatAmp,sameNo_of_amp_phase_length,part2 =None):

    xpiezo_nm = 1000*ampdf['Piezo']  # now xpiezo_nm in nm --> after multiplying by 1000 become in nm earlier ampdf['Piezo'] was in micro meter.
    x_diff = np.diff(ampdf['Piezo'])
    d_nm = 1000*x_diff[5]   # this is in nanometer (nm) now. 
    dataselect1 = zero_orFlatAmp
    # print("d in nm \t:",d_nm)
    # count = 0
    # for val in x_diff:
    #     # just to check common differences between piezo values.
    #     count = count+1
    #     print(val)
    #     if count ==5:
    #         break
            
    # plt.plot(list(range(len(x_diff))), ampdf['Piezo'])    
    # plt.show()
    # #     print()

    # here 2.5,3nm any value we put get corresponding N 
    # backward_MinimaBump_nmValue = 4.0  # <------------- make it as argument in func.
    N_count_back = (backward_MinimaBump_nmValue)/(d_nm)  # (using a+(n-1)D)

    N_count_back = np.ceil(N_count_back)
    print("n count back = ",N_count_back)

    desired_nmBackIndexwrtoInflexion = res_indices[0] - N_count_back  # it is from the inflexion point index_inflexion = index_inflexion - 4 
    # it has been seen in the results, index is shifted towards right,to compensate it just pull it left side.
    desired_nmBackIndexwrtoMinima = res_indices[1] - N_count_back  # this is from the minima point
    # desired_nmBackIndex
    # now time to choose the data 3nm after the minima(bump):
    # forward_MinimaBump_nmValue = 10.0     # <------------- make it as argument in func.
    
    N_count_forward = (forward_MinimaBump_nmValue)/(d_nm)  # (using a+(n-1)D)
    N_count_forward = np.ceil(N_count_forward)
    data_choose_endindex = res_indices[1] + int(N_count_forward)
    data_choose_endindex = data_endamp

    desired_nmBackIndexwrtoInflexion = int(desired_nmBackIndexwrtoInflexion)
    if desired_nmBackIndexwrtoInflexion < 0:
        desired_nmBackIndexwrtoInflexion = 0
        
    desired_nmBackIndexwrtoMinima = int(desired_nmBackIndexwrtoMinima)
    if desired_nmBackIndexwrtoMinima < 0:
        desired_nmBackIndexwrtoMinima = 0

    print("\n index starting wrto inflexion : ",desired_nmBackIndexwrtoInflexion, 
        "\n index starting wrto Minima : ",desired_nmBackIndexwrtoMinima)

    # desired_nmBackIndexwrtoInflexion = int(desired_nmBackIndexwrtoInflexion)
    # desired_nmBackIndexwrtoMinima = int(desired_nmBackIndexwrtoMinima)



    ##### ----------this is for linear fitting the data from desired point to the inflexion points data :-----------##
    # Perform linear regression for linear fitting
    index_inflexion = res_indices[0]   # < -- it is inflexion point 
    index_inflexion_new = index_inflexion - 4    # here as i have seen that inflexion index should be bit less than that we got, reduced by 4 index.
    ampdf_x_nm = 1000*ampdf['Piezo'][desired_nmBackIndexwrtoInflexion:index_inflexion_new]
    ampdf_y_nA = ampdf['Amplitude'][desired_nmBackIndexwrtoInflexion:index_inflexion_new]

    coefficients = np.polyfit(ampdf_x_nm,ampdf_y_nA, 1)

    m, c = coefficients
    # Print the results
    print(f"m (slope in nA/nm ): for {i+1} file data {m}")
    print(f"c, zero intercept nA (intercept): for {i+1} file data {c}")

    ampdf_y_nm = (1/m)*ampdf_y_nA    #--------****** save this data as Amplitude in .dat file----------*********** 

    poly = np.poly1d(coefficients)  # this is like f(x) = m*x + c , give x values get y values.

    # Plot the data and the linear fit
    fig, ax1 = plt.subplots()
    ax1.plot(ampdf_x_nm,ampdf_y_nm, marker ='.',markersize=2, linewidth=0.7, alpha=0.4,label='Data(nm)')
    ax1.set_xlabel('piezo(nm)')
    ax1.set_ylabel('Amplitude(nm)',color='b')
    ax1.tick_params('y', colors='b')  # this will make blue color font on y axis left side.
    ax1.grid()
    ax1.legend()

    ax2= ax1.twinx()  # it will share the x axis --> twinx()
    ax2.plot(ampdf_x_nm, ampdf_y_nA, color='green',marker ='.',markersize=2, linewidth=0.7, alpha=0.4,label='Data(nA)') #x, y, '.-', color='gray', markersize=2, linewidth=0.5, alpha=0.3, label='Smoothed Data
    ax2.plot(ampdf_x_nm, poly(ampdf_x_nm), color='red', label='Linear Fit') 
    ax2.set_xlabel('piezo(nm)')
    ax2.set_ylabel('Amplitude(nA)',color='r')
    ax2.tick_params('y',colors = 'r')
    ax2.set_ylim([6,10])
    # ax2.set_grid()
    ax2.legend(loc=[0.02,0.79])
    plt.title('Linear fitting of the ampltitude and piezo data')
    plt.show()


    # ************ ------------ this is working fine for me ----------------------******************
    # same data but another figure 

    fig
    # plt.scatter(ampdf_x_nm, ampdf_y_nA, marker ='.',markersize=1, linewidth=0.5, alpha=0.4,label='Data(nA)')
    plt.scatter(ampdf_x_nm, ampdf_y_nA, marker='.', s=1, linewidth=0.5, alpha=0.4, label='Data(nA)')

    # plt.scatter(ampdf_x_nm,ampdf_y_nm, marker ='*',markersize=1, linewidth=0.5, alpha=0.3,label='Data(nm)') # THIS IS FOR CONVERTED Y DATA TO nm --> y=  y*(1/m)
    plt.scatter(ampdf_x_nm,ampdf_y_nm, marker='*', s=1, linewidth=0.5, alpha=0.3, label='Data(nm)')

    plt.plot(ampdf_x_nm, poly(ampdf_x_nm), color='red', label='Linear Fit')

    plt.grid()
    plt.xlabel('piezo(nm)')
    plt.ylabel('Amplitude(nA)')
    plt.title('Linear fitting of the ampltitude and piezo data')
    plt.legend()
    plt.show()


    # ----------------******************************* this is the final data we will save in .dat file .------------------
    ampdata2saveAspiezo_nm = xpiezo_nm[desired_nmBackIndexwrtoInflexion:data_choose_endindex]   # data_choose_endindex --> it is the last index = dataendamp 979 
    print(ampdata2saveAspiezo_nm.head())
    # ampdata2saveAspiezo_nm = ampdata2saveAspiezo_nm + c/m
    ampdata2saveAspiezo_nm = ampdata2saveAspiezo_nm - ampdata2saveAspiezo_nm[desired_nmBackIndexwrtoInflexion] 

    ampdata2saveAsAmplitude_nm = (1/m)* ampdf['Amplitude'][desired_nmBackIndexwrtoInflexion:data_choose_endindex]

    print("amp data size:", ampdata2saveAsAmplitude_nm.shape)
    plt.plot(ampdata2saveAspiezo_nm,ampdata2saveAsAmplitude_nm,'-r')
    plt.grid()
    plt.xlabel('piezo(nm)')
    plt.ylabel('Amplitude(nm)')
    # plt.title('just to check before saving to .dat file')
    plt.title(f"just to check before saving to .dat file no. no.{i+1}/{sameNo_of_amp_phase_length}")
    # plt.legend()
    plt.show()


    # #  this is for the phase values:---------------------------------********


    print(phasedf.iloc[0,1]) # first value added -- phasedf.iloc[0,1]
    # last value add ---- > phasedf.iloc[data_endamp-1,1] 

    phase  = - phasedf['Phase'] -90 + phasedf.iloc[data_endamp-1,1]
    print("phase shape :\n", phase.shape)
    print("\n new phase values: \n", phase[0:5])

    phasedata2savedegree = phase[desired_nmBackIndexwrtoInflexion:data_choose_endindex]

    plt.plot(ampdata2saveAspiezo_nm,phasedata2savedegree,'-b')
    plt.grid()
    plt.xlabel('piezo(nm)')
    plt.ylabel('phase(o)')
    # plt.title('PHASE in degree just to check before saving to .dat file')
    plt.title(f"PHASE in degree just to check before saving to .dat file no.{i+1}/{sameNo_of_amp_phase_length}")
    # plt.legend()
    plt.show()

# <----------------------------any data can select depend on the starting and ending points given in arguments or defined above. ---------------- >
    # <------------------ use these two as base and select any data part from this here phase in degree and ampdf in nm. ------------- >
    # ampdata2saveAsAmplitude_nm = (1/m)* ampdf['Amplitude']    # <---- in nm  
    # phasedata2savedegree = phase                              # <----- in degree 
    
    ampfrominflexion2flat_nm = (1/m)* ampdf['Amplitude'][index_inflexion:dataselect1]  # dataselect1 = zero_orFlatAmp
    phasefrominflexion2flat_degree = phase[index_inflexion:dataselect1]                #  dataselect1 = zero_orFlatAmp
    piezofrominflexion2flat_nm  = ampdata2saveAspiezo_nm[index_inflexion:dataselect1]   # <--- this is the final data to save as piezo in nm.

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

    # # now generate a .dat file from the where data is saved ( unit: nm)
    return (ampdata2saveAspiezo_nm,ampdata2saveAsAmplitude_nm,phasedata2savedegree,ampfrominflexion2flat_nm,phasefrominflexion2flat_degree,piezofrominflexion2flat_nm,m)