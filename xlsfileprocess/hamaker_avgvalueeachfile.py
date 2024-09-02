import pandas as pd
import os

def save_avg_hamaker(data_path, result_list, output_filename="avg_hamaker_results.xlsx"):
    df = pd.DataFrame(result_list, columns=['filename', 'avg_hamaker'])
    output_path = os.path.join(data_path, output_filename)
    df.to_excel(output_path, index=False)
    print(f"Average Hamaker values saved to {output_path}")



# result_list.append((res_hamaker[0], res_hamaker[1]))

# # Save all results to an Excel file
# save_avg_hamaker(data_path, result_list)

# def save_avg_hamaker(data_path, filenames, avg_hamaker_values):
#     """
#     Save average Hamaker values and corresponding filenames to an Excel file.
    
#     Parameters:
#     - data_path (str): The path where the Excel file will be saved.
#     - filenames (list of str): List of filenames corresponding to the average Hamaker values.
#     - avg_hamaker_values (list of float): List of average Hamaker values.
#     - output_filename (str): The name of the output Excel file.
#     """
#     # Create a DataFrame with filenames and avg_hamaker_values
#     df = pd.DataFrame({
#         'Filename': filenames,
#         'Avg_Hamaker_Value': avg_hamaker_values
#     })
    
#     # Create the directory if it doesn't exist
#     if not os.path.exists(data_path):
#         os.makedirs(data_path)
    
#     # Define the full path for the Excel file
#     excel_file_path = os.path.join(data_path,'avg_hamaker_values.xlsx')
    
#     # Save the DataFrame to an Excel file
#     df.to_excel(excel_file_path, index=False)


# if __name__ == "__main__":
#     data_path = "datac\\hamaker_results"
#     filenames = ['file1.mat', 'file2.mat', 'file3.mat']
#     avg_hamaker_values = [1.23, 2.34, 3.45]
#     # output_filename = "avg_hamaker_values.xlsx"
    
#     save_avg_hamaker(data_path, filenames, avg_hamaker_values)
