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