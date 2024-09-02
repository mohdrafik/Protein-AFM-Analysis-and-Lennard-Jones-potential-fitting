""" this is for the extract information from the random text data need to arrange the data in a format of 3 columns according to the information: but in my given data file 
data is arranged like one line data then one blank line then data then one blank line and so on...
here my purpose is to do --> these 3 consecutive data lines(not blank lines) in one row and so on.. 
"""

# path = "C:\\Users\\mrafik\\Desktop"
with open('newregu.txt','w') as newreg:
    with open('regularexp.txt','r') as regfile:
        count = 0
        lines = regfile.readlines()  # read all the data at once from the file regularexp.txt in lines and returns them as a list. ['Line 1\n', 'Line 2\n', 'Line 3\n']
        print("--------------------- new output ----------------------------------------------------------------")
        listoflines = []
        for line in lines:
            print(line)
            count = count+1
            line = line.strip()  # The strip() method removes leading and trailing whitespaces, including newline characters, from the string.
            
            if (count+1) % 2 == 0:   # this is for to choose the alternative line including first line (like 1,3,5,7,9,11,13 ...)
                print(count,"writing data")
                lengthofline = len(line)
                listoflines.append(line+(40-lengthofline)*" ")   # this is for giving the equal space  from the starting (i.e = 40,including the previous string) or to align the each column in the output file.
                # print("data of lists ---> ",listoflines)  

                # newreg.writelines(line)
                if ((count+1)%6 == 0):  # selecting the relevent count before going to the next line.(3 content line + 2 blank line between them )
                    print("writing next line ")
                    newreg.writelines(listoflines)
                    newreg.write('\n')     # going to the next line after each row completion ( after writing 3 list elements.) 
                    listoflines = [] # Reset the list after writing
                # if count==23:
                #     break


print("<----------------for read line by line ---------------------->")
with open('newregu.txt','r') as fread:
    line = fread.readlines()
with open('newfilewithhash.txt','w') as fw:    
    for contentline in line:
        newcontent = "\t## "+ contentline
        # print("#"+ contentline)
        fw.write(newcontent)
        if contentline == line[-1]:
            print("---------------> ",contentline)
            break                