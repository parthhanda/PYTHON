amt = int(input("enter the amount to be withdrawn - "))

hundred = amt//100
amt = amt % 100

fifty = amt//50
amt = amt % 50

ten = amt//10

print("Number of hundred notes - ",hundred)
print("Number of fifty notes - ",fifty)
print("Number of ten notes - ",ten)