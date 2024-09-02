import pandas as pd
import numpy as np
import os
from termcolor import colored

def hamaker_save_data(data_path, ampdf_data_nm, phasedf_degree, piezodf_data_nm, filenameAmplitude, filenamephase, A0, K = None, Q = None, R = None):
    # hamaker constant from inflexion to end of dataframe (endAmp) or general calculation depends on your data.
    ampdf_data_nm = ampdf_data_nm.reset_index(drop=True)
    phasedf_degree = phasedf_degree.reset_index(drop=True)
    piezodf_data_nm  = piezodf_data_nm.reset_index(drop=True)

     # Ensure that the DataFrames have the same length
    min_length = min(len(ampdf_data_nm), len(phasedf_degree), len(piezodf_data_nm))
    ampdf_data_nm = ampdf_data_nm[:min_length]
    phasedf_degree = phasedf_degree[:min_length]
    piezodf_data_nm = piezodf_data_nm[:min_length]
    
    
    # Convert values to meters and radians
    amp_df_meter = ampdf_data_nm*1e-9 
    piezo_df_meter = piezodf_data_nm*1e-9
    # phase_df_radian = np.radians(phasedf_degree)
    phase_df_radian = np.deg2rad(phasedf_degree)
    
    # Calculate Hamaker values  here A0 = A0 in meter.
    # hamaker_values = ((-3 * K * A0) / (Q * R)) * ((amp_df_meter ** 2) * np.cos(phase_df_radian)) * ((((piezo_df_meter + amp_df_meter) / amp_df_meter) ** 2) - 1) ** 1.5 # phase taken in radian

    hamaker_values = ((-3 * K * A0) / (Q * R)) * ((amp_df_meter ** 2) * np.cos(phasedf_degree)) * ((((piezo_df_meter + amp_df_meter) / amp_df_meter) ** 2) - 1) ** 1.5  # phase taken in degree 

    
    avg_hamaker = np.average(hamaker_values)  # average value of hamaker dataframe.
   

    # Create DataFrame with columns 'piezo', 'amplitude', 'phase', and 'hamaker_values'
    df = pd.DataFrame({
        'piezo_meter': piezo_df_meter.values.flatten(),
        'amplitude_meter': amp_df_meter.values.flatten(),
        'phase_degree': phasedf_degree.values.flatten(),
        'phase_radian': phase_df_radian.values.flatten(),
        'hamaker_values': hamaker_values.values.flatten()
    })

    # df = pd.DataFrame({
    #     'piezo_meter': piezo_df_meter,
    #     'amplitude_meter': amp_df_meter,
    #     'phase_degree': phasedf_degree,
    #     'phase_rad': phase_df_radian,
    #     'hamaker_values': hamaker_values
    # })


    # Create directory 'hamaker_data' if it doesn't exist
    hamaker_dir = os.path.join(data_path, 'hamaker_data')
    if not os.path.exists(hamaker_dir):
        os.makedirs(hamaker_dir)

    # Save DataFrame to Excel file in 'hamaker_data' directory
    # hamaker_filename = filenameAmplitude[0:-5]+filenamephase[0:-5]+'hamaker.xlsx'
    
    hamaker_filename = filenameAmplitude[:-5] + filenamephase[:-5]+"hamaker.xlsx"
    excel_file_path = os.path.join(hamaker_dir, hamaker_filename)
    df.to_excel(excel_file_path, index=False)
    
    return hamaker_filename, avg_hamaker, hamaker_values 
    
# Example usage
if __name__ == "__main__":
    data_path = "datac\\"
    amp = pd.DataFrame([i for i in range(5)])
    pdf = pd.DataFrame([p for p in range(0, 50, 10)])
    pds = pd.DataFrame([d for d in range(6, 11, 1)])
    print("all data and see", amp, pdf, pds)
    ampfilename = 'ampl.xlsx'
    phasefilename = 'phas.xlsx'
    A0 = 20
    K = 50
    Q = 40
    R = 1
    hamaker_save_data(data_path, amp, pdf, pds, ampfilename, phasefilename, A0, K, Q, R)


"""
# this was old used for -->  this will calculate hamaker from inflexion(just before bump) to zero_flatAmp 

def hamaker_save_data(data_path, ampdf_data_nm, phasedf_degree, piezodf_data_nm, filenameAmplitude, filenamephase, A0, K = 2.56, Q = 234, R = 10e-9):
    
    ampdf_data_nm = ampdf_data_nm.reset_index(drop=True)
    phasedf_degree = phasedf_degree.reset_index(drop=True)
    piezodf_data_nm  = piezodf_data_nm.reset_index(drop=True)
    
    # Convert values to meters and radians
    amp_df_meter = ampdf_data_nm*1e-9 
    piezo_df_meter = piezodf_data_nm*1e-9
    # phase_df_radian = np.radians(phasedf_degree)
    phase_df_radian = np.deg2rad(phasedf_degree)

    # Calculate Hamaker values  here A0 = A0 in meter.
    hamaker_values = ((-3 * K * A0) / (Q * R)) * ((amp_df_meter ** 2) * np.cos(phase_df_radian)) * ((((piezo_df_meter + amp_df_meter) / amp_df_meter) ** 2) - 1) ** 1.5

    # Create DataFrame with columns 'piezo', 'amplitude', 'phase', and 'hamaker_values'
    df = pd.DataFrame({
        'piezo_meter': piezo_df_meter,
        'amplitude_meter': amp_df_meter,
        'phase_degree': phasedf_degree,
        'phase_rad': phase_df_radian,
        'hamaker_values': hamaker_values
    })

    # Create directory 'hamaker_data' if it doesn't exist
    hamaker_dir = os.path.join(data_path, 'hamaker_data')
    if not os.path.exists(hamaker_dir):
        os.makedirs(hamaker_dir)

    # Save DataFrame to Excel file in 'hamaker_data' directory
    # hamaker_filename = filenameAmplitude[0:-5]+filenamephase[0:-5]+'hamaker.xlsx'
    
    hamaker_filename = filenameAmplitude[:-5] + filenamephase[:-5]+"hamaker.xlsx"
    excel_file_path = os.path.join(hamaker_dir, hamaker_filename)
    df.to_excel(excel_file_path, index=False)


"""