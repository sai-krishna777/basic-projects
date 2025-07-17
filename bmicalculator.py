#BMI calculator

print("*__BMI calculator__*")
weight = float(input("enter the body weight in kilograms (kg): "))
height = float(input("enter the height in meters (m) : "))
age = int(input("enter your age : "))
gender = input("enter your gender : ")

bmi = weight /(height ** 2)
print(f"your bmi is {bmi:.2f}")

if bmi<18.5:
   print("category : underweight")
   suggested_calories = 2500 if gender == "male" else 2000
   print(f"suggested daily calorie intake = {suggested_calories+300} kcal (to gain weight)")
elif 18.5 <= bmi < 24.9 :
   print("category : normal weight")
   suggested_calories = 2500 if gender == "male" else 2000
   print(f"suggested daily calorie intake = {suggested_calories} kcal (to gain weight)")
elif 25 <= bmi <29.9 :
   print("category : over weight")
   suggested_calories = 2500 if gender == "male" else 2000
   print(f"suggested daily calorie intake = {suggested_calories-300} kcal (to gain weight)")
else :
   print("category : obese weight")
   suggested_calories = 2500 if gender == "male" else 2000
   print(f"suggested daily calorie intake = {suggested_calories+500} kcal (to gain weight)")

print("\nNote: This is a general estimate. For personalized advice, consult a nutritionist.")