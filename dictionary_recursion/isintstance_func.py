"""
here some example of isinstance() function of the dictionary object, 3 example is given 
which wiol be used in later examples. 
"""

d = {'a': {'b': {'c': 1, 'd': 2}}, 'e': {'f': 3}}
print(d.keys())
print(d.values())
x = d.items()
'''item() give the content of the dictionary
in the list of tuple pair of key and value.'''
print(type(x))
''' if isinstance(value, dict)  --> here isinstance object(value) is type of the given class or instance of that class. 
isinstance(object,classinfo) function in Python is used to check if an object belongs to a specified class
or is an instance of a specified class or a tuple of classes.
'''
'''example 1'''
x = 10
if isinstance(x,int):
    print('TRUE')
else:
    print("False")    

'''example 2'''
y = [1,23,3]
if isinstance(y,(list,tuple)):
    print("Return TRue")
else:
    print("return False")
        
'''Example 3:'''
class Myclass:
    pass
obj = Myclass()

if isinstance(obj,Myclass):
    print("I am True")
else:
    print("I am not True")