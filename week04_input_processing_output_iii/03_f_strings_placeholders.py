# ------------------------------------------------------------------------------
# Placeholders can be used to insert the value of a given variable or named
# constant.
# ------------------------------------------------------------------------------

item = 'Health Potion'
fstring2 = f'You found a {item}!'
print(fstring2)

print()

amount_due = 5000.0
monthly_payment = amount_due / 12.0
print(f'If {amount_due} is the total, then the monthly payment is {monthly_payment}.')