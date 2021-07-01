'''Your Life in Weeks.

Instructions
I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

https://waitbutwhy.com/2014/05/life-weeks.html

Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

Example Input
56
Example Output
You have 12410 days, 1768 weeks, and 408 months left.
e.g. When you hit run, this is what should happen:

https://cdn.fs.teachablecdn.com/RjqBViZQpyVTv7XY6cfA

Hint
There are 365 days in a year, 52 weeks in a year and 12 months in a year.
Try copying the example output into your code and replace the relevant parts so that the sentence is formated the same way.'''

def age_calculator():
    print("Welcome to my age calculator in days, weeks and months!\n")
    user_name = input("Please, enter your name: ")
    
    while True:
        try:
            user_age = int(input("Please, enter your age: "))

            days = 365
            weeeks = 52
            months = 12

            years_to_live = 90 - user_age
            result_days = years_to_live * days
            result_weeks = years_to_live * weeeks
            result_months = years_to_live * months
        
            print(f"Hello {user_name}! If you get to live 90 years, then you have {result_days} days, {result_weeks} weeks, and {result_months} months left.")

        except:
            print("Please, enter a digital number.")
            continue

        else:
            break


age_calculator()
