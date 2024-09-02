import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


def sliced_data_min_zero_potential_force_and_index(distance,potential, startindex, endindex, no_timesofwhm_beforeminima,no_timesofwhm_afterminina):
    """
    Find the index of the minimum potential
    no_timesofwhm_beforeminima = 3  # leave it open to choose in function arguments.
    no_timesofwhm_afterminina = 5 # leave it open to choose in function arguments.
    this function returns the values. sliced_distance,sliced_potential,start_index,end_index,min_index

    """
    
    smoothed_potential = potential
    min_index = np.argmin(smoothed_potential) # make the potential smooth before giving to the this function.

    # Define HWFM function
    def hwfm(y):
        half_max = (np.max(y) - np.min(y)) / 2 + np.min(y)
        peaks, _ = find_peaks(-y)  # Inverting y to find valleys
        if len(peaks) > 0:
            closest_peak = peaks[np.argmin(np.abs(peaks - min_index))]
        else:
            closest_peak = min_index
        half_max_index = np.where(y[:closest_peak] >= half_max)[0]
        if len(half_max_index) > 0:
            hwfm_index = half_max_index[-1]
        else:
            hwfm_index = closest_peak
        return hwfm_index

    # Compute HWFM index
    hwfm_index = hwfm(smoothed_potential[:min_index])

    # Start index: before the minima using HWFM
    if startindex is None:
        start_index = min_index - no_timesofwhm_beforeminima*hwfm_index
    else:
        start_index = startindex  

    # End index: after the minima by 10 times the HWFM
    if endindex is None:
        end_index = min_index + no_timesofwhm_afterminina * hwfm_index
    else:
        end_index = endindex

    # Ensure indices are within bounds
    start_index = max(start_index, 0)
    end_index = min(end_index, len(smoothed_potential) - 1)

    # Slice the potential and distance data
    sliced_distance = distance[start_index:end_index]
    sliced_potential = smoothed_potential[start_index:end_index]

    # Plot the sliced data
    plt.figure(figsize=(10, 6))
    plt.plot(distance, smoothed_potential, label='Smoothed Potential', color='blue')
    plt.plot(sliced_distance, sliced_potential, label='Sliced Potential', color='red')
    plt.axvline(x=distance[min_index], color='green', linestyle='--', label='Minima')
    plt.axvline(x=distance[start_index], color='orange', linestyle='--', label='Start HWFM')
    plt.axvline(x=distance[end_index], color='purple', linestyle='--', label='End HWFM')
    plt.xlabel('Distance')
    plt.ylabel('Potential')
    plt.title('Slicing Potential Data Based on HWFM')
    plt.legend()
    plt.show()

    return sliced_distance,sliced_potential,start_index,end_index,min_index

if __name__=="__main__":
    # Load the data
    data = pd.read_csv('smooth_data.csv')
    distance = data['distance'].values
    potential = data['potential'].values
    sliced_data_index = sliced_data_min_zero_potential_force_and_index(distance,potential,no_timesofwhm_beforeminima=10,no_timesofwhm_afterminina=20)
    
