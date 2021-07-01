'''BMI Calculator

Instructions
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv

Warning you should convert the result to a whole number.

Example Input
weight = 80
height = 1.75
Example Output
80 ÷ (1.75 x 1.75) = 26.122448979591837

26
e.g. When you hit run, this is what should happen:

https://cdn.fs.teachablecdn.com/wmjVjddeSmGj0QVtOUrE

Hint
Check the data type of the inputs.
Try to use the exponent operator in your code.
Remember PEMDAS.
Remember to convert your result to a whole number (int).'''

# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in m: "))
# result = weight / (height * height)


# print(result)

# Body Mass Index (BMI) Calculator.

def user_bmi():
    print("Welcome to Body Mass Calculator made by Abdul Aziz.\n")
    while True:
      try:
          height = float(input("Enter your height in meters: "))
          weight = int(input("Now enter your weight in kilograms: "))
          bmi = round(weight/ (height * height), 1)
      
          if bmi <= 18.5:
              print('Your BMI is', bmi, 'which means you are underweight. You need some protein.')

          elif bmi > 18.5 and bmi < 25:
              print('Your BMI is', bmi, 'which means you are normal. You are fit and looking good! :)')

          elif bmi > 25 and bmi < 30:
              print('Your BMI is', bmi, 'which means you are overweight. You need some exercise.')

          elif bmi > 30:
              print('Your BMI is', bmi, 'which means you are obese. Keep exercising... You can do this!')

      except:
          print("Lets start from beginning. Please, enter your height in meters and make sure it is in digital number.")
          continue

      else:
          break

user_bmi()



# Another solution:

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

weight_as_int = int(weight)
height_as_float = float(height)

# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)

print(bmi_as_int)