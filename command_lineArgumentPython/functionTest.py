# import numpy 

# def add(a,b):
#     return a+b

# def sub(a,b):
#     return a-b

# def div(a,b):
#     return a/b

# def mult(a,b):
#     return a*b

v1 = [1,2,3]
v2 = [3,7,8]

# sum =[]

# def addlist(a,b):
#     # sum =0
#     for i in range(len(a)):
#         sum = a[i]+b[i]
#         sumlist.append(sum)
#         sum = 0

#     return sumlist
# def dot(v1, v2):
#     sum =0
#     m = 0
#     for i in range(len(v1)):
#         m = v1[i]*v2[i]
#         sum = sum+m
#     return sum

# res = dot(v1,v2)
# print("sum of list:",res)

"""
Write a function add_n that takes a single numeric argument n, and returns a function. 
The returned function should take a vector v as an argument and return a new vector with the value for n added to each element of vector v. 
For example, add_n(10)([1, 5, 3]) should return [11, 15, 13].

A = [[1, 2, 3], [-2, 3, 7]]
>>> B = [[1,0,0],[0,1,0],[0,0,1]]
>>> array_mult(A, B)
[[1, 2, 3], [-2, 3, 7]]

"""

def array_mult(A, B):
    
    rows_A = len(A)
   
    cols_A = len(A[0])
    
    cols_B = len(B[0])
    
   
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result


