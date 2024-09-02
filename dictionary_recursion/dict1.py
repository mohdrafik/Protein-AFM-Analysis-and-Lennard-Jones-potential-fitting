'''
# problem: Using dictionary comprehension, 
create a new dictionary with only the key-value pairs where the values are even.
'''
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
new_dict = {}
for key,val in original_dict.items():
    if val%2==0:
        new_dict[key] = val 
        
        
print(new_dict)        

