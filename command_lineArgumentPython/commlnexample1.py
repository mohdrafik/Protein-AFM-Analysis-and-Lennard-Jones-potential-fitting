import argparse
def addition(datapath,out_path,param1,param2):

    sum2num = param1+param2;
    sum2num = str(sum2num)
    print("output sum is :",sum2num)
    with open(datapath+'outfile.txt','w') as fw:
        fw.write(sum2num)

# if __name__ == "__main__":



