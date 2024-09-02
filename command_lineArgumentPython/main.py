""" 
PS E:\python_programs\command_lineArgumentPython> python main.py --a 30 --b 50 

in this we can run the program from the terminal.

"""

import argparse
import functionTest as ft

Parser = argparse.ArgumentParser(description="calling the function from another module and passing the arguments from main")

Parser.add_argument('--b',type=int,required= True,help=" give a integer value")
Parser.add_argument('--a',type=int,required= True, help=" give a another integer value")

args = Parser.parse_args()

print(f"\n add res:{ft.add(args.a,args.b)}\n subtraction res:{ft.sub(args.a,args.b)}") 
print(f"\n division res:{ft.div(args.a,args.b)}\n multiplication res:{ft.mult(args.a,args.b)}") 



# import argparse
# import commlnexample1 as ex1


# parser = argparse.ArgumentParser(description='basic example for addtion')
# parser.add_argument('--datapath', type=str, required=True,help='path to input file' )
# parser.add_argument('--out_path', type=str, required=True,help='path to save the output file' )
# parser.add_argument('--param1', type=int, required=True,help=' first parameter' )
# parser.add_argument('--param2', type=int, required=True,help=' second parameter ' )

# args = parser.parse_args()
# ex1.addition(args.datapath,args.out_path,args.param1,args.param2)



"""  both way we can do it like above written line or below written line also work."""

# # def main(data_path,out_path,param1,param2):
# def main():
#     parser = argparse.ArgumentParser(description='basic example for addtion')
#     parser.add_argument('--datapath', type=str, required=True,help='path to input file' )
#     parser.add_argument('--out_path', type=str, required=True,help='path to save the output file' )
#     parser.add_argument('--param1', type=int, required=True,help=' first parameter' )
#     parser.add_argument('--param2', type=int, required=True,help=' second parameter ' )

#     args = parser.parse_args()

#     ex1.addition(args.datapath,args.out_path,args.param1,args.param2)

# if __name__ =="__main__":
#     main() 

    




"""
    parser.add_argument('--input_path', type=str, required=True, help='Path to the input data file')
    parser.add_argument('--output_path', type=str, required=True, help='Path to save the processed data')
    parser.add_argument('--param1', type=int, required=True, help='First processing parameter')
    parser.add_argument('--param2', type=float, required=True, help='Second processing parameter')

    args = parser.parse_args()
"""