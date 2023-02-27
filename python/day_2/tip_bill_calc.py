print("Welcome to the tip calculator.")
print("What is the total bill? ")
bill = float(input())

party = int(input("How many people dined? "))

tip_percent = int(input("What percentage would you like to tip? "))
tip = round(tip_percent/100, 2)*bill

total = (bill + tip)

split_bill = round(total/party, 2)
print("Each person pays $" + str(split_bill))