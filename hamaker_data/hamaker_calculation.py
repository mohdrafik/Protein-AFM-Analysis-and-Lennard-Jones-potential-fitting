import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
import math
import os

def hamaker_const(datapath, filename, start_idx, end_idx, hamdeg = None ):

    """
    if hamdeg is None --> then calculate the cos_phi in Radian. otherwise in degree.
    give you datapath only program will process all files one by one.. 
    I think the hamaker in joule, give you datapath 
    K= 26.90  # N/m
    Q= 466
    R = 10  #nm
    Piezo Amp near distant in meter
    if you are not getting nothing in some column it means it is infinite or NAN

    """
    # df_nd = pd.read_excel('408 with neardistance.xlsx')
    # df_nd = pd.read_excel("408 with piezo.xlsx")
    file2read = os.path.join(datapath,filename)
    
    # df_nd = pd.read_excel(file2read)
    df_nd = pd.read_csv(file2read,delimiter=' ')
    # df_nd = df_nd[start_idx:end_idx]

    # for col in df_nd.columns:
    #     print(col)
    #     if col =="piezo":
    #         distancekey = "piezo"
    #     elif col == "piezo ":
    #         distancekey = "piezo "
    #     elif col == "neardistance ":
    #         distancekey = "neardistance "
    #     elif  col == "neardistance":
    #         distancekey = "neardistance"
    #     else:
    #         print("----------- May be new key is there just check :----->")
            

    # print(df_nd.head() ,"and size:\n ",df_nd.shape,"\n", df_nd.tail(),"\n")   # Piezo Amp near distant in meter

    K= 26.90  # N/m
    Q= 466
    # R = 10  # nm 
    R = 10*1e-9  # m now after convert from nm 
    A0 = df_nd['amplitude'].iloc[-1]
    K_constant = -(3*K*A0)/(Q*R)

    df_nd = df_nd[start_idx:end_idx]   # here it is sliced according to strat and end index.

    phase_deg = df_nd["phase"]
    df_nd["phase_radian"] = np.deg2rad(df_nd["phase"])

    # cosphi = [ math.cos(phase) for phase in df_nd['phase']]  # when by default phase in degree
    # phase_radians = [math.radians(phase) for phase in df_nd['phase']]  # here phase converted to radian
    # cosphi_rad = [ math.cos(phase) for phase in phase_radian]
    # cos_phi = np.cos(phase_radian)
    
    if hamdeg is not None:
        # cos_phi_deg = np.cos(phase_deg)
        cos_phi = np.cos(phase_deg)  # is not None 1,2,3 degree
        print( " !!!!!!cos_phi values is taken in degrre ------->")

    else:
        cos_phi = np.cos(df_nd["phase_radian"])  # None hai to radian
        print( " !!!!!! cos_phi values is taken in Radian ------>")

        
    
    # print(f"A_cosphi \n:{cos_phi}  and\n  --> Phase in radians: \n {1},\n {phase_deg} \n {df_nd} ")

    Asqu_multi_cosphi = df_nd['amplitude']**2 *cos_phi   # Asqu_multi_cosphi = df_nd['amplitude']**2 *(cos_phi)
    # last_term = ((df_nd["neardistance"]/df_nd["amplitude"] + 1)**2  - 1 )**1.5
    # last_term = ((df_nd[distancekey]/df_nd["amplitude"] + 1)**2  - 1 )**1.5
    # last_term = ((df_nd['piezo']/df_nd["amplitude"] + 1)**2  - 1 )**1.5  

    ifcomplex_part_lastTerm = ((df_nd['piezo']/df_nd["amplitude"] + 1)**2  - 1)  # last term is less than zero 
    ifcomplex_part_lastTerm = np.abs(ifcomplex_part_lastTerm)   # making it positive 
    last_term = (ifcomplex_part_lastTerm)**1.5   # sepeartly

    # last_term = ((df_nd['piezo']/df_nd["amplitude"] + 1)**2  - 1 )**1.5  
    # last_term = np.abs(last_term)

    df_nd['last_term']  = last_term
    ham_cons = K_constant * Asqu_multi_cosphi*last_term  # hm = - (3 * k * A0 * A**2 * math.cos(phi) / (Q * R)) * (((d + A) / A)**2 - 1)**(3/2)

    df_nd["ham_const"] = ham_cons
    ham_cons_avg = np.mean(ham_cons)
    df_nd["ham_cons_avg"] = ham_cons_avg

    print(f"ham constant :{ham_cons} and \n{ham_cons.shape} and \n \n ----> hawmaker average value:\n {ham_cons_avg}")
    ham_consfilename = "hamaker_data"+filename[0:-4]+".xlsx"
    ham_consfilenamefinal = os.path.join(datapath,ham_consfilename)
    df_nd.to_excel(ham_consfilenamefinal)

    res = {
            "filename":filename[0:-4],
            "hamaker_const":ham_cons_avg
           }
    return res
    # df_nd2 = df_nd['amplitude'] -(1.65*ones_array) 
    # print("df2: ",df_nd2.head())
    # plt.figure()
    # plt.subplot(2,1,1)
    # plt.plot(df_nd['neardistance'], df_nd['amplitude'] -(1.65e-8) )  
    # plt.grid(True)
    # plt.subplot(2,1,2)
    # plt.plot(df_nd['neardistance'], df_nd['amplitude']) 
    # plt.grid(True)
    # # plt.plot(df_nd['neardistance'],df_nd['phase'])

if __name__=="__main__":
    
    filename_list = []
    hamaker_constavglist = []

    datapath = "E:\\python_programs\\xlsfileprocess\\hamaker_data\\hamdata\\"
    # datapath = "E:\python_programs\xlsfileprocess\hamaker_data\hamdata"
    for filename in os.listdir(datapath):
        print("<------------------------------->",filename)
        # if filename[-5:] ==".xlsx" and filename[0:7] !='hamaker':
        if filename[-4:] ==".dat" and filename[0:7] !='hamaker':
            print(f"----------->!!!!!!!! current processing file name is {filename}") 
            result = hamaker_const(datapath,filename, hamdeg= None)

            filename_list.append(result["filename"])
            hamaker_constavglist.append(result["hamaker_const"])

    hamaker_constavgData = {"filename":filename_list,"hammaker_constant":hamaker_constavglist}

    hamaker_constavgData_df = pd.DataFrame(hamaker_constavgData)

    hamaker_constavgData_df.to_excel(os.path.join(datapath,'hamaker_avgValeachfile.xlsx'))        


    """
    If hamdeg is None --> calculate the codphi in Radian. Otherwise in degree.
    Processes all files in the given datapath.
    # """
    # file2read = os.path.join(datapath, filename)
    # df_nd = pd.read_excel(file2read)
    
    # # Identify the correct column for distance
    # distancekey = None
    # for col in df_nd.columns:
    #     if col.strip() in ["piezo", "piezo ", "neardistance", "neardistance "]:
    #         distancekey = col
    #         break
    
    # if distancekey is None:
    #     print("No valid distance column found in the file.")
    #     return 
    
#     df_nd["phase_radian"] = np.deg2rad(df_nd["phase"])
    
#     if hamdeg is not None:
#         cos_phi = np.cos(df_nd["phase"])
#         print("!!!!!! cos_phi values are taken in degrees ------->")
#     else:
#         cos_phi = np.cos(df_nd["phase_radian"])
#         print("!!!!!! cos_phi values are taken in radians ------->")
    
#     # Calculate the Hamaker constant
#     Asqu_multi_cosphi = df_nd['amplitude']**2 * cos_phi
#     last_term = ((df_nd[distancekey] / df_nd["amplitude"] + 1)**2 - 1)**1.5
    
#     # Ensure no division by zero or invalid operations
#     valid_indices = np.isfinite(last_term) & np.isfinite(Asqu_multi_cosphi)
#     ham_cons = np.full(df_nd.shape[0], np.nan)  # Initialize with NaNs
#     ham_cons[valid_indices] = K_constant * Asqu_multi_cosphi[valid_indices] * last_term[valid_indices]
    
#     df_nd["ham_const"] = ham_cons
#     ham_cons_avg = np.nanmean(ham_cons)
#     df_nd["ham_cons_avg"] = ham_cons_avg

#     print(f"ham constant :{ham_cons} and \n{ham_cons.shape} and \n \n ----> hamaker average value:\n {ham_cons_avg}")
    
#     ham_consfilename = "hamaker_data_" + filename[:-5] + ".xlsx"
#     ham_consfilenamefinal = os.path.join(datapath, ham_consfilename)
#     df_nd.to_excel(ham_consfilenamefinal)
    
#     res = {
#         "filename": filename[:-5],
#         "hamaker_const": ham_cons_avg
#     }
#     return res

# if __name__ == "__main__":
#     filename_list = []
#     hamaker_constavglist = []

#     datapath = "E:\\python_programs\\xlsfileprocess\\hamaker_data\\"
#     for filename in os.listdir(datapath):
#         print("<------------------------------->", filename)
#         if filename.endswith(".xlsx") and not filename.startswith('hamaker'):
#             print(f"current processing file name is {filename}")
#             result = hamaker_const(datapath, filename)

#             if result:  # Check if result is not None
#                 filename_list.append(result["filename"])
#                 hamaker_constavglist.append(result["hamaker_const"])

#     hamaker_constavgData = {"filename": filename_list, "hammaker_constant": hamaker_constavglist}
#     hamaker_constavgData_df = pd.DataFrame(hamaker_constavgData)
#     hamaker_constavgData_df.to_excel(os.path.join(datapath, 'hamaker_avgValeachfile.xlsx'))
