days = int(input("How many days rented?"))
Km = float(input("How many kilometers rented?"))
Pay = (days * 60) + (Km * 0.15)
print("The total amount payable for kilometers driven and US${:.2f}".format(Pay))

