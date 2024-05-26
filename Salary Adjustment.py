Salary = float(input("What is the employee's salary? $"))
NewSalary = Salary + (Salary * 15 / 100)
print("An employee who earns ${:.2f} with a 15% increase starts to receive ${:.2f}".format(Salary, NewSalary))
