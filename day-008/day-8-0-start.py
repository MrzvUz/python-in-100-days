# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# Simple function with no paramenters and arguments.
def greet():
    print("Hello, world")
    print("Hello, world")
    print("Hello, world")

greet()


# Function with one name parameter and "Ali" argument.
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}?")

greet_with_name("Ali")


# Function with more than 1 parameter(input).
def greet_with(name, location): # inside the perentcis are colled paramenters.
    print(f"Hello, my name is {name} and I am from {location}!")

greet_with("Ali", "USA") # These are folled arguments.
greet_with(name = "Ali", location = "USA") # And these are called Positional Arguments.

