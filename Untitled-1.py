# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height1 = float(height)
weight1 = int(weight)

bmi = (weight1 / (height1 **2))

print (int(bmi))