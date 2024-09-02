'''
This function is called,again and again in for loop, which draw the histogram of each seperated data(.mat file) using the  k -means cluster.    
'''
import scipy.io as sio
import os 
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram_auto(data, filename):
    """
    Create a histogram with automatic bin width and edges chosen from the data.
    
    """
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    binsw = (max(data) -min(data))/200 
    # Automatically calculate bin edges based on data distribution
#     counts, bin_edges, _ = plt.hist(data, bins='auto')  #stdval = 0.0045
    counts, bin_edges, _ = plt.hist(data, bins=100,edgecolor='black')  #stdval = 0.0045
    plt.xlabel('Value')
    plt.ylabel('Frequency')
#     plt.xlim([1.31,1.48])
    plt.title(filename)

    # Identify and label extreme values
#     mean_count = np.mean(counts)
#     std_count = np.std(counts)
#     extreme_values = []
#     for i, count in enumerate(counts):
#         if count > mean_count + 2 * std_count or count < mean_count - 2 * std_count:
#             plt.text(bin_edges[i], 0, str(round(bin_edges[i], 2)), rotation=90, va='bottom', ha='center', color='red')
#             extreme_values.append(bin_edges[i])

    # Save the figure
    filename1 = filename+'.png'
    print(filename1)
    plt.savefig(filename1, dpi=300, bbox_inches='tight')
    # Show the plot
    plt.show()
    # plt.close()
# plot_histogram_auto(data, 'histogram.png')

path = r'C:\Users\mrafik\Desktop\conference_data\conference_data'

# for mat in os.path.join(path,.mat):

allfiles = os.listdir(path)
matfiles = []
count = 0
for filename in allfiles:
  
    if filename.endswith('.mat'):
        count =count+1
        matfiles.append(filename)
        print(filename)
#         readmatfile(filename)
        datastruct = sio.loadmat(filename)
        data = datastruct['mat_temp']
        data = np.array(data)
        data = data.flatten()
        data = data[data!=0]
        filename = filename[0:-4:1]+'py'
        print("new file name after detele .mat = ", filename)
        print("max data :",max(data), " ","min data", min(data))
        print("figure completed and size type of data--> ",count,data.size,data.dtype)    
        plot_histogram_auto(data, filename)  # This function is called,again and again in for loop, which draw the histogram of each seperated data(.mat file) using the  k -means cluster.    
        
      
        

