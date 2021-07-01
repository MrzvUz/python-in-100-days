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