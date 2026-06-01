#PROBLEM: Calculate income tax for a given income based on these rules:

#First $10,000: 0% tax
#Next $10,000: 10% tax
#Remaining income: 20% tax

#PURPOSE:This exercise introduces “Tax Brackets” logic, a classic example of complex conditional branching. It shows how to calculate values cumulatively instead of applying a single percentage to the entire amount.

income = 45000
tax_payable = 0
print("Given income:",income)

if income  <= 10000:
    tax_payable = 0
elif income <= 20000:
    tax_payable = (income - 10000) * 10 /100
else: 
    tax_payable = 0 + (10000 * 10 /100)

    tax_payable += (income - 20000) * 20 /100

print("Total income tax to pay: {}".format(tax_payable))