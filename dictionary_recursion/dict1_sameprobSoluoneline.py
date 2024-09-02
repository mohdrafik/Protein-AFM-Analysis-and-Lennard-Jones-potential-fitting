'''
# problem: Using dictionary comprehension, create a new dictionary with only the key-value pairs where the values are even.
ONE LINE SOLUTION FOR THE PROBLEM
'''
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
new_dic2 = {key: val  for key,val in original_dict.items() if val%2==0 }
'''
new_dic2 = { } # create the new empty dictionary. 
then key:val , corresponding key and value assigned by the dict item list if val is even.   
 
'''
print(new_dic2)