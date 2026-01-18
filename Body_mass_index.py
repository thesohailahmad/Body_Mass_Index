# Body Mass Index
gender = input("Enter your gender Male/Female :")
age = int(input("Enter your age: "))
Weight = int(input("Enter your weight in Kg :"))
Height = float(input("Enter your height in Meter :"))
BMI = Weight / ( Height * Height)
print( "---Results---" )
print( " Gender : " , gender )
print( " Age : ", age )
print( " Your BMI is " , round(BMI,2))
if BMI < 18.5:
    print( "Underweight" )
elif BMI < 25:
    print( "Healthy" )
elif BMI < 30:
    print("Overweight")
elif BMI < 35:
   print( "Obesity Class 1" )
elif BMI < 40:
   print( "Obesity Class 2" )
else:
   print( "Obesity Class 3 Severe" )