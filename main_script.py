"""
module_script.py defines a greet function and checks if it is being run as the main program 
using if __name__ == "__main__". If it's the main program, it asks the user for their name and greets them. 
If it's imported as a module into another script (like main_script.py), 
the code block under if __name__ == "__main__" is not executed.
"""
import module_script
# Call the greet function from module_script
msg = module_script.greet("veto rana reddy")
print(msg)
