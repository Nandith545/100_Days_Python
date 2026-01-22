# Author: Nandith Malapati

weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in meters:"))

bmi = weight / (height ** 2)

if bmi < 18.5 :
    print("underweight")
elif bmi >= 18.5 and bmi < 25 :
    print("normal weight")
else:
    print("overweight")
