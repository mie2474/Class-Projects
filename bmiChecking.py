#BMI Calculator
print ("This Program Calculates Body Mass Index(BMI)")
print ("-------------------------------------------")
x = int(input("Enter your weight: " ))
weight = (x / 2.205)    #convert  weight from lbs to kg
y = int(input("Enter your height in ft: "))
height = (y * 12)       #Convert height from ft to inches

z = int(input ("Enter your inches: "))#get inches of the height for total height inches
#convert total inches to meter(m)
ft = (z + height) * 0.0254
ft_in = height + z

#Get bmi formula 
bmi = (weight / (ft ** 2))

print ("\nYour weight in 'kg' is:", weight)
print ("Your height in 'm' is:", ft)
print ("Your height in 'ft' is:", ft_in, "\n")

#if, else statement to set range for user to know his/her BMI
if bmi < 18.5:
    print ("Your BMI is:", bmi, "UNDERWEIGHT")
elif bmi <= 24.9:
    print ("Your BMI is:", bmi, "NORMAL WEIGHT")
elif bmi <= 30:
    print ("Your BMI is:", bmi, "OVERWEIGHT")
else:
    print ("Your BMI is:", bmi, "OBESE")
