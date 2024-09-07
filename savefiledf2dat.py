from termcolor import colored
import pandas as pd
import numpy as np
def filesaveDatain_dat(directory_path,ampdata2saveAspiezo_nm,ampdata2saveAsAmplitude_nm,phasedata2savedegree,filenameAmplitude,filenamephase,hamakerConstant = None, A0= None):
    if hamakerConstant == None:
        df1 = ampdata2saveAspiezo_nm*1E-9  #  converted to m 
        df2 = ampdata2saveAsAmplitude_nm*1E-9 # converted to m 
        df3 = phasedata2savedegree  #  in degree 
        print("\n",df1.shape,"\n",df2.shape, "\n",df3.shape)
        combined_df = pd.concat([df1,df2,df3], axis=1)  
        print(colored("Below this is before reverse and scientific notation and deletion: \n",'green', attrs=['bold']),combined_df.head())

        # from here start process for 1. delete the first row 2. denote in the scientific notation 3. reverse and add header in combined_df

        combined_df = combined_df.iloc[1:]   # 1.

        combined_df = combined_df.apply(lambda x: x.apply(lambda y: f'{y:.9E}'))  # 2. Format data in scientific notation

        combined_df = combined_df[::-1] # 3.-- Reverse DataFrame

        combined_df.columns = ['piezo', 'amplitude', 'phase']   # 3.--- Add headers

        print(colored("without heading or column index next we will see with index: \n",'green', attrs=['bold']),combined_df.head())
        # Reset index
        combined_df.reset_index(drop=True, inplace=True)

        print(colored("after final procees:\n",'green', attrs=['bold']),combined_df.head())

        # Concatenate the DataFrames vertically
        # combined_df = pd.concat([df1,df2,df3], axis=1)
        # Save the combined DataFrame to a .dat file

        
        filename = filenameAmplitude.strip('.')[0:-5]+filenamephase.strip('.')[0:-5]+".dat"
        combined_df.to_csv(directory_path+filename, sep=' ', index=False, header=True)

        print(colored(f" \n HELLO ! <----------  file are saved in .dat format with name:{filename} ---------->  ",'green', attrs=['bold']))
      
    if hamakerConstant == 1:
        K = 2.56
        Q = 234
        R = 10*10E-9
        A0 = A0
        print("<--**************************---------inside the calculation hawmaker constant:  -------------***************** >",A0,hamakerConstant)

        df1 = ampdata2saveAspiezo_nm*1E-9  #  converted to m 
        df2 = ampdata2saveAsAmplitude_nm*1E-9 # converted to m 
        df3_degree = phasedata2savedegree
        df3 = phasedata2savedegree*((np.pi)/180)  #  in now in radian

        df4 = ((-3*K*A0)/(Q*R))*((df2**2 )*np.cos(df3))*((((df1+df2)/df2)**2) -1)**1.5   # rewrite this formula carefully and check..

        print(" here check the dimensions match or nor !!!!!!!!  - inside the hamakerConstant = 1 --> ","\n",df1.shape,"\n",df2.shape, "\n",df3.shape,"\n",df4.shape)

        combined_df = pd.concat([df1,df2,df3_degree,df3,df4], axis=1)  
        print(colored("Below this is before reverse and scientific notation and deletion: \n",'green', attrs=['bold']),combined_df.head())

        # from here start process for 1. delete the first row 2. denote in the scientific notation 3. reverse and add header in combined_df

        combined_df = combined_df.iloc[1:]   # 1.

        combined_df = combined_df.apply(lambda x: x.apply(lambda y: f'{y:.9E}'))  # 2. Format data in scientific notation

        # combined_df = combined_df[::-1] # 3.-- Reverse DataFrame   # not reversed in case of the hamaker uncomment if you want to reverse data.

        combined_df.columns = ['piezo', 'amplitude','phase(degree)', 'phase(rad)','hamakerConstant' ]   # 3.--- Add headers

        print(colored("without heading or column index next we will see with index: \n",'green', attrs=['bold']),combined_df.head())
        # Reset index
        combined_df.reset_index(drop=True, inplace=True)

        print(colored("after final procees:\n",'green', attrs=['bold']),combined_df.head())

        # Concatenate the DataFrames vertically
        # combined_df = pd.concat([df1,df2,df3], axis=1)
        # Save the combined DataFrame to a .dat file

        filenamehawmaker = filenameAmplitude.strip('.')[0:-5]+filenamephase.strip('.')[0:-5]+"hamaker"+".dat"
        combined_df.to_csv(directory_path+filenamehawmaker, sep=' ', index=False, header=True)

        print(colored(f" \n HELLO ! <----------  file are saved in .dat format with name:{filenamehawmaker} ---------->  ",'green', attrs=['bold']))
    
    return  filename
    
    # # Save the combined DataFrame to a .dat file
    # combined_df.to_csv('combined_data.dat', sep=' ', index=False)
   

    