import os
# data_path =  "dataproblem\\"
def listxlsFiles(data_path):
    listOfFiles = os.listdir(data_path)
    # print(listOfFiles)
    amp_seperate_list = []
    phase_seperate_list = []
    for file in listOfFiles:
        if file[-5:] =='.xlsx':
            if file[0:9] =="Amplitude":
                print("amplitude:",file[9:-5],end=' | ')
                num_Subscript = file[9:-5]
                num_Subscript_num = file[9:-5]
                amp_seperate_list.append(file)
                flag = 0
                for file in listOfFiles:
                    if file[0:5] == "phase" and file[5:-5] == num_Subscript:
                        flag += 1
                        print("pahse:",file[5:-5])
                        phase_seperate_list.append(file)

                if flag == 0:
                    print(f"!! --> For amplitude {num_Subscript_num} phase:{num_Subscript_num} file NOT FOUND ! ----> ",num_Subscript_num)

    print("\n",amp_seperate_list,"\n length of the amp list -->",len(amp_seperate_list))
    print("\n",phase_seperate_list,"\n length of the phase list -->",len(phase_seperate_list))
    l1= amp_seperate_list
    l2= phase_seperate_list
    return l1,l2
if __name__ == "__main__":
    # data_path =  "dataproblem\\"
    data_path =  "dataproblem\\curvesongold\\"
    listxlsFiles(data_path)