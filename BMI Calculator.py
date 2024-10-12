#BMI = Weight in kgs / (height in m)^2

weight = float(input("Enter weight in kgs: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height*height)
print("BMI is:  " + str(bmi))