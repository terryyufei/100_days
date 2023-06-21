# Review: 
# Create a function called greet(). 
# Write 2  print statements inside the function.
# Call the greet() function and run your code.
'''
def greet():
    print("Hello Sophia!")
    print("Welcome to the first day of the rest of your life!")
    
greet() 
'''   
   
#functions with inputs
'''
def greet(name):
    print("Hello {} :)".format(name))
    print("Welcome to the first day of the rest of your life!")
    

greet("Sophia")  
'''  
#functions with mutiple inputs && positional arguments
'''
def greet(name, location):
    print(f"Hello {name} :)")
    print("Welcome to the first day of the rest of your life!")
    print(f"Are you happy to be in {location}?") 

greet("Sophia", "ALX")
'''

#functions with keyword arguments

def greet(location = 'ALX', name = 'Soph'):
    print(f"Hello {name} :)")
    print("Welcome to the first day of the rest of your life!")
    print(f"Are you happy to be in {location}?") 

greet()