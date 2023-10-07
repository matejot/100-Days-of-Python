print ("Welcome to the tip calculator")

total_cost = input("what was the total bill? ")

percantage_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")

people = input("How many people to split the bill? ")

#Calculating both the total cost plus the tip percentage
per_person = float(total_cost) * int(percantage_tip) / 100
#print (total)

total = round((per_person + float(total_cost)) / int(people), 2)

print (f"Each person should pay: {total}")
