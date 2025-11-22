# Rent Calculator Project

# Input from user
rent = int(input("Enter your flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total units of electricity = "))
charges_per_unit = int(input("Enter the charges per unit = "))
persons = int(input("Enter the number of persons living in flat = "))

# Calculation
total_bill = electricity_spend * charges_per_unit
output = (rent + food + total_bill) // persons

# Final Output
print("Each person will pay = ", output)