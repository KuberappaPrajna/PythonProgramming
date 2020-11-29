weight = int(input("Enter the weight?"))
height = float(input("Enter the height?"))

BMI = int(weight / height ** 2)

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

if BMI < 18.5:
  print(f"your BMI is {BMI} you are underweight")
elif BMI > 18.5 and BMI < 25:
  print(f"your BMI is {BMI} you are normal weight")
elif BMI > 25 and BMI < 30:
  print(f"your BMI is {BMI} you are slightly overweight")
elif BMI > 30 and BMI < 35:
  print(f"your BMI is {BMI} you are obese")
else:
  print(f"your BMI is {BMI} you are clinically obese")