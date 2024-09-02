def greet(name):
    return f"hi My name is {name}, welcome {name}!!!!"
if __name__ == "__main__":
    name = input("enter a name")
    msg = greet(name)
    print(msg)
    