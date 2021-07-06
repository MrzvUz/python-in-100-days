programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again"
    }


# Retrieving items from dictionary.
print(programming_dictionary["Function"])
print(programming_dictionary.keys())
print(programming_dictionary.values())
print(programming_dictionary.items())


# Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again"


# Creating an empty dictionary.
empty_dictionary = {}


# Wiping an existing dictionary.
programming_dictionary = {}
# print(programming_dictionary)


# Edit an item in a dictionary.
programming_dictionary["Bug"] = "New Value"


# Loop through a dictionary.
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
