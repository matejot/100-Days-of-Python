print("Thank you for choosing Python Pizza Deliveries!")
size = input("Size") # What size pizza do you want? S, M, or L
add_pepperoni = input("Pepperoni") # Do you want pepperoni? Y or N
extra_cheese = input("extra cheese") # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
price = 0

if size == "S":
  price += 15
  
elif size == "M":
  price += 20
elif size == "L":
  price += 25

if add_pepperoni == "Y":
    if size == "S":
      price += 2  
    else:
      price += 3

if extra_cheese == "Y":
  price += 1


print (f" Your final bill is: ${price}.")