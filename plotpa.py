import pandas as pd
import matplotlib.pyplot as plt
import os 

# path = "E:\\python_programs\\xlsfileprocess\\dataproblem\\new_data7sep24\\processdata\\"
# path = "E:\\Protein-AFM-Analysis-and-Lennard-Jones-potential-fitting\\data\\processdata\\"
path = r"E:\Protein-AFM-Analysis-and-Lennard-Jones-potential-fitting\data\processdata"

listfiles = os.listdir(path) 
print(listfiles)

# plt.figure
count = 0 
for file in listfiles:
    if file.endswith('.dat'):
        print(file)
        count = count +1
        filename = os.path.join(path,file)
        # df = pd.read_csv(path+file,delimiter=' ')
        df = pd.read_csv(filename,delimiter=' ')
        print(df.head())
        # plt.figure()
        plt.plot(df['piezo'],df['amplitude'])
plt.show()
        # if count ==1:
        #     break
        # plt.legend()



