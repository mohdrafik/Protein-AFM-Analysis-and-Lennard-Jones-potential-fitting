# import argparse

# parser = argparse.ArgumentParser(description= "passing the arguments")

# parser.add_argument("echo",type = int,help ='square of the number')

# args = parser.parse_args()

# print(args.echo**2)
# # parser.add_argument("echo")
import os
import scipy.io as sio
import numpy as np

def readfiles(datapath,savepath):

    listfiles = os.listdir(datapath)

    for file in listfiles:
        if file.endswith('.mat'):

            datastruct = sio.loadmat(datapath+file)
            data = datastruct['mat_temp']  # data is structred with name mat_temp
            data = np.array(data)
            data = data.flatten()
            data = data[data!=0]
            filename1 = file[0:-4:1]+'minmaxdata'
            maxdata = max(data)
            mindata = min(data)
            str1 = f"filename:{filename1} maxdata :{maxdata} and mindata :{mindata} \n"
            print("new file name after detele .mat = ", filename1)
            print("max data :",max(data), " ","min data", min(data))
            with open(savepath+'out.txt','a+') as f:
                f.write(str1)

            # print("figure completed and size type of data--> ",data.size,data.dtype)   
if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser("pass the save and data path")

    parser.add_argument("--datapath",type = str, help =" enter the data path for reading the .mat file")
    parser.add_argument("--savepath",type = str, help =" enter the save path for reading the .mat file")

    args =parser.parse_args()

    readfiles(args.datapath,args.savepath)
    


             
            







