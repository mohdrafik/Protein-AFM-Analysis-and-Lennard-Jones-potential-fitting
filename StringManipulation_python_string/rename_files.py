import os
import argparse

def renameFile(path):
    """
    use command terminal,  give path for the files which need to be renamed
    here I am using .pdf file, which will be renamed.
    """
    listdir = os.listdir(path)
    for file in listdir:
        if file.endswith('.pdf'):
            try:
                new_name = file.split("_",1)[1]  # split the name in two parts as list index 0,1
            except IndexError :
                print("index does not exist or '_' does not exits.")
                new_name = file               
            try:
                os.rename(path+file,path+new_name)
            except FileExistsError:
                new_name = file
                os.rename(path+file,path+new_name)

            # os.rename(file,new_name)
            print(f"{file} is renamed to {new_name}")
    return f"files renamed succesfully:"        

if __name__=="__main__":

    parser = argparse.ArgumentParser(description="enter arg")
    parser.add_argument("-path",type=str,required= True, help="enter jsut any thing str")
    parser.add_argument("-a",type=str,help = " enter name")
    args = parser.parse_args()
    msg = renameFile(args.path)

    print(f"here in driver function --->: {msg}")
