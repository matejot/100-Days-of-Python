# Which year do you want to check?
year = int(input("Type year "))
# 🚨 Don't change the code above 👆
#on every year that is divisible by 4 with no remainder
#except every year that is evenly divisible by 100 with no remainder
#unless the year is also divisible by 400 with no remainder
# Write your code below this line 👇
if year % 4 == 0:
  print ("Leap year")  
  if year % 100 == 0:
    print ("Not leap year")
    
else:
  print ("Not leap year")
    