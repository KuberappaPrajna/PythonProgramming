weight = input("What is your weight?")
height = input("What is your height?")

int_weight = int(weight)
int_height = float(height)
BMI_value = int_weight/(int_height*int_height)
BMI = int(BMI_value)

print("BMI =" +str(BMI))