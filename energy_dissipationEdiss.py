import pandas as pd
import numpy as np
import os
from termcolor import colored

def energy_dissipation(data_path, ampfrominflexion2flat_nm, phasefrominflexion2flat_degree, piezofrominflexion2flat_nm, filenameAmplitude, filenamephase, A0, K = None, Q = None):
    
    ampfrominflexion2flat_nm = ampfrominflexion2flat_nm.reset_index(drop=True)
    phasefrominflexion2flat_degree = phasefrominflexion2flat_degree.reset_index(drop=True)
    piezofrominflexion2flat_nm  = piezofrominflexion2flat_nm.reset_index(drop=True)
    
    # Convert values to meters and radians
    amp_df_meter = ampfrominflexion2flat_nm / 1e9
    piezo_df_meter = piezofrominflexion2flat_nm / 1e9
    phase_df_radian = np.radians(phasefrominflexion2flat_degree)
    phase_df_degree = phasefrominflexion2flat_degree

    # Calculate Hamaker values
    # E_diss = ((np.pi * K * amp_df_meter**2) / Q) * (((A0 / amp_df_meter) * np.sin(phase_df_radian)) - 1)
    E_diss = ((np.pi * K * amp_df_meter**2) / Q) * (((A0 / amp_df_meter) * np.sin(phase_df_degree)) - 1)
    E_diss = E_diss * 6.242e18
    
    # hamaker_values = ((-3 * K * A0) / (Q * R)) * ((amp_df_meter ** 2) * np.cos(phase_df_radian)) * ((((piezo_df_meter + amp_df_meter) / amp_df_meter) ** 2) - 1) ** 1.5

    # Create DataFrame with columns 'piezo', 'amplitude', 'phase', and 'hamaker_values'
    df = pd.DataFrame({
        'piezo_meter': piezo_df_meter,
        'amplitude_meter': amp_df_meter,
        'phase_degree': phasefrominflexion2flat_degree,
        'phase_rad': phase_df_radian,
        'phase_degree':phase_df_degree,
        'Energy_dissipation(eV)': E_diss
    })

    # Create directory 'hamaker_data' if it doesn't exist

    energy_dissipation = os.path.join(data_path, 'energy_dissipation_data')
    if not os.path.exists(energy_dissipation):
        os.makedirs(energy_dissipation)

    # Save DataFrame to Excel file in 'energy_dissipation_data' directory
    
    
    energy_dissi_filename = filenameAmplitude[:-5] + filenamephase[:-5]+"energy_dissi.xlsx"
    excel_file_path = os.path.join(energy_dissipation, energy_dissi_filename)
    df.to_excel(excel_file_path, index=False)
    
    return E_diss