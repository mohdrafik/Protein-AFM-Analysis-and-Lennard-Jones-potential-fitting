"""Shift + Enter run the current cell, select below
Ctrl + Enter run selected cells
Alt + Enter run the current cell, insert below
Ctrl + S save and checkpoint"""

import pandas as pd
import numpy as np
import os
import math
from scipy.integrate import quad
import matplotlib.pyplot as plt
def potential_force_algo(data_path,filename):
    # excel_path = "E:\\python_programs\\xlsfileprocess\\dataproblem\\"
    # excel_path = "C:\\Users\\mrafik\\Desktop\\python_general_code\\xlsfileprocess\\"
    # excel_path = "/media/mrafik/Drive/python_programs/xlsfileprocess/"
    excel_path = data_path
    # excel_path+filename
    # here xls file is read
    df = pd.read_csv(excel_path+filename,delimiter=' ')
    # df = pd.read_excel(
    #     '/home/mrafik/Desktop/C_codeAniqa/2023-AM-AFM-Spectroscopy/2023-AM-AFM-Spectroscopy/Spectroscopy/FRAME_20230418.xls',
    #     usecols='A:F')
    print(" read the .dat file processed \n",df.head(5))

    print(" ------------****** Reading of the data excel file is over ------------******\n")
    p = df['phase']  # p phase is a vector
    A = df['amplitude']         # A --> amplitude
    pi_val = math.pi
    c_z = 2.756  # --> it is in N/m spring constant , he was using 40
    # c_z = 2.756e-9   # now in N/nm spring constant
    fd = 72.7163e3
    f0 = 72.7163e3
    D_min = min(df['piezo'])
    Qfactor = 241
    aexc = max(A) / Qfactor 
    # aexc = 220e-9/Qfactor

    def Kvalue(A_i, P_i):
        """
        call the function in a loop, it will calculate the
        k value for each phase and amplitude value taken from the
        aniqa data.
        """
        k = (0.5) * (((aexc / A_i) * (math.cos((P_i * pi_val) / 180))) - ((f0 ** 2 - fd ** 2) / f0 ** 2))
        return k


    # ********* code for potential U integration ***********
    # import numpy as np

    def integration(A_i, P_i):
        k = (0.5) * ((aexc / A_i) * (math.cos((P_i * pi_val) / 180)) - ((f0 ** 2 - fd ** 2) / f0 ** 2))
        
        def u(t):  ## Define the integrand function
            return (4 * c_z * k * (t ** 3 + ((((A_i) * (t ** 2)) / 16 * pi_val) ** 0.5) + ((((A_i) ** 3) ** 0.5) / ((2) ** 0.5))))
        
        integral_value, error = quad(u, 0.001, 10e12, weight='cauchy', wvar=0)
        
    #     integral_value, error = quad(u, 0, np.inf, weight='cauchy', wvar=0)
    #     integral_value, error = quad(u, 0, np.inf)   # this is working 1st.
        #  print("The value of the integral and error is:", integral_value,error)
        #     print(integral_value,error)
        return integral_value

    print("------------****** Integration is done ------------******\n ")
    # ********* code for writing data in the file ***********


    #*************** force using k expression.**********

    def Force_integrating_K(A_i, P_i):
        def k_exp(zeta = c_z):
            return (0.5) * (((aexc / A_i) * (math.cos((P_i * pi_val) / 180))) - ((f0 ** 2 - fd ** 2) / f0 ** 2))*(2*zeta)
        integral_value, error = quad(k_exp, D_min, 10, weight='cauchy', wvar=0)
        #     integral_value, error = quad(u, 0, np.inf, weight='cauchy', wvar=0)
    #     integral_value, error = quad(u, 1, np.inf)   # this is working 1st.
        #     print("The value of the integral and error is:", integral_value,error)
    #     print(integral_value,error)
        return integral_value

    # ********* code for writing data in the file ***********

    # potential= []
    import csv
    # Open the CSV file in write mode.
    filename = "force_potentialkval.csv"
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["piezo", "potential(U)", "Kvalue","integral_usingK"]) 
        # Write the header row
        for i in range(len(p)):           # Write data in each iterative loop
            kval = Kvalue(A[i],p[i])
    #         if i<3:
    #             print("kval = ",kval)
            integral_U = integration(A[i], p[i])
    #         print("after integration argument=",kval)
            Force_usingK = Force_integrating_K(A[i], p[i])
        
            writer.writerow([df['piezo'][i], df['amplitude'][i], integral_U, kval,Force_usingK])
            # Write the iteration and data as a row

    print("Data saved in", filename)
    csvfile.close()

    # df_datoutspec = pd.read_csv(
    #     '/home/mrafik/Desktop/C_codeAniqa/2023-AM-AFM-Spectroscopy/2023-AM-AFM-Spectroscopy/Spectroscopy/spec_dataout_aniqadat.csv')
    # df_datoutspec = pd.read

    df_datoutspec = pd.read_csv('force_potentialkval.csv')

    # df_datoutspec = pd.read_csv(
    #     '/home/mrafik/Desktop/C_codeAniqa/2023-AM-AFM-Spectroscopy/2023-AM-AFM-Spectroscopy/Spectroscopy/spec_dataout_aniqa.csv')
    # df_datoutspec = pd.read_csv("spec_dataout_aniqa.csv")
    # df_datoutspec.head(3)
    print(f"------------****** data file: {filename} is created and data is read from the written file {filename} for plotting and analysis ------------****** ")
    # df_idx = df_datoutspec['potential(U)'].idxmax()

    # print("index of max = ",df_idx)
    # print("val at max idx = ",iloc.df_datoutspec[df_idx,])

    # ********** normalization ***********
    # df_U = df_datoutspec['potential(U)']
    # df_U =(df_U - df_U.min())/(df_U.max() - df_U.min())

    # ********** normalization using std ***********
    # df_U = df_datoutspec['potential(U)']
    # df_U =(df_U - df_U.mean())/df_U.std()
    # # df =(df - df.mean())/df.std()
    # df_U


    # df_datoutspec['potential(U)'].iloc[df_idx]  # to find the max value at the df_idx index(row)
    # df_datoutspec.drop(df_idx,axis =0,inplace =True)
    # k = []
    # for i in range(len(p)):
    # #      k1 = (0.5) * ((aexc / A[i]) * (math.cos((p[i] * pi) / 180)) - ((f0 ** 2 - fd ** 2) / f0 ** 2))
    #     val =  Kvalue(A[i],p[i])
    #     k.append(val)

    # df_datoutspec['potential(U)']

    # ********* for plotting the Kvalue and U  ..

    # df_plot = pd.read_csv('/home/mrafik/Desktop/C_codeAniqa/2023-AM-AFM-Spectroscopy/2023-AM-AFM-Spectroscopy/Spectroscopy/spec_dataout_aniqa.csv')

    fig1 = plt.figure("Figure 1")
    # plt.figure(figsize=(4, 3))
    plt.plot(df_datoutspec['piezo'],df_datoutspec['Kvalue'], '-b')
    plt.xlabel('distance')
    plt.ylabel('k value')
    plt.title('K VALUES vs NUMBERS')
    # plt.ylim([0.0010,0.0035])
    plt.show()

    print("plotting for k value is done")
    # ********* for plotting U  ..

    print("------------****** plotting for potential value is going on ..........")

    fig2 = plt.figure("Figure 2")
    # plt.figure(figsize=(4, 3))
    # plt.plot(df_datoutspec['distance(D-A)(nm)'], df_U, '-r')
    plt.plot(df_datoutspec['piezo'], df_datoutspec['potential(U)'], '-r')
    plt.xlabel('distance(D)')
    plt.ylabel('potential')
    plt.title('potential vs piezo')

    # plt.ylim([0.0010,0.0035])
    # plt.xlim([-17.0,-14])
    plt.show()

    print(" ------------******  plotting for potential value is done ------------****** ")
    # this is for the differentiation  for Force calculation *****
    print("------------******  differentiation for force is going on ------------****** ")
    # Convert dataframes to NumPy arrays

    x = df_datoutspec['piezo'].values
    # y = df_U.values
    y = df_datoutspec['potential(U)']

    # Perform numerical differentiation
    dy_dx = np.gradient(y, x)

    # Create a new dataframe for the differentiation result
    differentiation_result = pd.DataFrame({'dy_dx': dy_dx})

    # Plot the result
    fig3 = plt.figure("Figure 3")
    plt.plot(x, dy_dx, '-m')
    plt.xlabel('Distance')
    plt.ylabel('F = force(i.e. dU/dD)')
    plt.title('Force = Numerical Differentiation Result')
    # plt.xlim([-17.0,-16.4])
    plt.show()


    # ************** FORCE PLOTTED using K ********************

    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True

    # plt.plot(df_datoutspec['piezo'].sort_values(),df_datoutspec['integral_usingK'] , '. m')
    # plt.plot(df_datoutspec['piezo'].sort_values(),df_datoutspec['integral_usingK'] , '. m')
    plt.plot(df_datoutspec['piezo']*(1.0e9),df_datoutspec['integral_usingK'] , '.-m')
    # plt.plot(df_datoutspec['integral_usingK'] , '-sm')
    # plt.tight_layout
    # plt.xlim([0.7e-8,1.4e-8]) # if Force plot is w.r.to Distance. 
    # plt.xlim([10,30])  # if Force plot is without any Distance, just raw plot 
    ll =  list(range(len(df['piezo'])))
    xx=np.zeros(len(ll))

    plt.plot(df_datoutspec['piezo']*(1.0e9),xx,'y-.')
    # plt.tight_layout()
    plt.xlabel('Distance(nm)')
    plt.ylabel('F = force(i.e. dU/dD)')
    plt.xlim([min(df_datoutspec['piezo']*(1.0e9)),max(df_datoutspec['piezo']*(1.0e9))]) # if Force plot is w.r.to Distance. 
    plt.title('Force = Numerical Differentiation Result')

    plt.show()

    print("------------ program is executed ------------ ")