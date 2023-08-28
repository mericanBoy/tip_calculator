# Write your code here :-)
#tip calculator
#take the input and store to variables
bill = input("what was the total bill? ")
tip = input("would you like to tip 10, 12 or 15 percent? ")
people = input("How many people are splitting the bill? ")
#get the tip value
tip_value = float(bill) / 100 * float(tip)
#calculate the total bill
tot_bill = float(bill) + float(tip_value)
#divide amongst every person
your_bill = tot_bill / float(people)
print(f"Each person should pay {round(your_bill, 2)}")
