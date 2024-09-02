"""

sets support x in set, len(set), and for x in set. Being an unordered collection, 
sets do not record element position or order of insertion. Accordingly, 
sets do not support indexing, slicing, or other sequence-like behavior.
set and its functions
set does not have repeated the value.
set object is not iterable
(set4(i)) --> TypeError: 'set' object is not callable and  not subscriptable, 

common_elements.intersection_update(value)  
# common_elements is a set which update, with the common elements(intersection of both set) in value set and common_elements set. 
"""
x = int(input("enter 1 for simple set example:, 2 for the another example of set:"))
match x:
   case 1:
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    set3 = {3, 4, 5}

    # common_val = set1    #empty set
    common_val = set1.intersection(set2,set3)  
    print(common_val)
   case 2:
        set1 = {1, 2, 3,6,7,8,9,0}
        set2 = {2, 3, 4,1,7,9,0}
        set3 = {3, 4, 5,7,9,0,1}
        set4 = {3, 4, 5,7,9,0,1,88,12,1,2,9}

        common_setval = set1.intersection(*[set2,set3,set4])  # intersection of all the 4 sets.
        print(common_setval)
   case _:
        print("no match cases:")
            
