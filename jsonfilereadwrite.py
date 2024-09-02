import json 
x = ['mahira',1,2,3,4,5]  # here we see any object data is converted to its JSON string representation. 
print(type(x))
y = json.dumps(x)
print(y)
print(type(y))   # <class 'str'>  We can see type of y is str. x object is converted to the json string.  

# reading the json file data .
with open('jsondata.txt','w+') as jfw:
    json.dump(x,jfw)  # here x object data is written in text file.
    jfw.read()

# here we will see, how we read the data from the json file.
# import json
with open('complex_data.json','r+') as file:   #   here fisrt we open json file and make an object to this as file. 
    data_loaded = json.load(file)  # here loaded the file using json.load(file)



