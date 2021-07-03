states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]


states_of_america[1] = "Pencilveniya" # Changes the items in the list in index 1.
states_of_america.append("Aliland") # Adds only one item at the end of the list.
states_of_america.extend(["Myland", "Yourland", "Hisland"]) # Adds multiple list items at the end of the list.

num_states = len(states_of_america) # Gives the number of items in the list.
states_of_america[num_states-1] # When you pass index of num_states variable in states_of_america then you have to add -1 to get the result, otherwise there would be out_of_range error.

print(states_of_america)
print(num_states)
print(states_of_america)





dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes", "Spinach", "Kale"]

fruits = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Tomatoes", "Celery", "Potatoes", "Spinach", "Kale"]

dirty_dozen_joined = [fruits, vegetables] # Joines two lists together and gives nested list with seperate fruits and vegetables lists inside one list.

print(dirty_dozen_joined)
