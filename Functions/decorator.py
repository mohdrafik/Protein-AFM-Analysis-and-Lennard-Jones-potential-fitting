# @decorator
def greet(fx):
    def mfx(*arg,**kwarg):
        print("good morning user!")
        fx(*arg,**kwarg)
        print("thanks for using the code function!")
    return mfx

@greet
def hello():
    print("hello world !------------------>")

hello()   

@greet
def add(a,b):
    print("hello world ! I am adding function")
    print(a+b)
    # return a+b
   

add(2,3)  

# greet(hello())   # both way we can write hello() or greet(hello())

# # @decorator
# def greet(fx):
#     def mfx():
#         print("good morning user!")
#         fx()
#         print("thanks for using the code function!")
#     return mfx

# @greet
# def hello():
#     print("hello world !")

# hello()   
# # greet(hello())   # both way we can write hello() or greet(hello())
