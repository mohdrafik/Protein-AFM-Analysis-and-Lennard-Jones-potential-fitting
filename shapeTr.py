def tree(height):
    length = height*2 -1
    stars = 1
    for i in range(1,height + 1):
        print(("*" * stars).center(length))
        stars +=2
    print("*".center(length))    

if __name__ =="__main__":
    height = int(input("enter height of the triangle >= 2:"))
    tree(height)

# import os
# data_path = "E:\\Protein-AFM-Analysis-and-Lennard-Jones-potential-fitting\\data\\"
# # datapath = "E:\\Protein-AFM-Analysis-and-Lennard-Jones-potential-fitting\\data\\processdata\\"
# datapath1 = os.path.join(data_path,'processdata\\')
# print("new------>",datapath1)
# print(os.listdir(datapath1))