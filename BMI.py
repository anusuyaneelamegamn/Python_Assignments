weight= int(input("Enter the weight in kg" ))
height =int(input("Enter the height in cm" ))
height = height/100
print(height)
height1 = (height*height)
print(height1)
BMI = weight / (height*height)
BMIINDEX = int(input("Enter the BMI Index" ))
if (BMIINDEX<18):
    print("Underweight")
elif(BMIINDEX>18.5 and BMIINDEX<24.9):
    print("Healthy")
elif(BMIINDEX>25 and BMIINDEX<29.9):
    print("Over weight")
elif (BMIINDEX>30):
    print("Very overweight")
