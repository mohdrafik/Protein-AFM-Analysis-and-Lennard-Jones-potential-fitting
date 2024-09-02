def greet(name):
    print("I am inside the function only")
    return f"hi {name} !!! My name is Moh Rafik ! , you are most Welcome {name} !)"
if __name__ == "__main__":
    print("inside the main function here __name__ = __main__ ")
    name = input("enter a name: ")
    msg = greet(name)
    print(msg)
    