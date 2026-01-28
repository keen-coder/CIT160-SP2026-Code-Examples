# ------------------------------------------------------------------------------
# Named constants are values in a program that are not supposed to change.
# Most other programming languages enforce this behavior, but Python does not.
# The only way to make a constant in your program is to name the constant
# using all caps. This is a formal agreement between you and the user of your code
# that the value of that name should not change. 
#
# Named constants are used to give an identifier to your values that would otherwise
# have to be repeatedly hardcoded throughtout your program
#
# Constants are good to write near the top of your program, that way if a value does
# need to change, you only need to make the change in one place.
# ------------------------------------------------------------------------------

# Examples of contants that should not change.
PI = 3.15159265
RADIUS_OF_EARTH = 6371 #km
E = 2.7182818284 # Euler's number

# Below is an example of constants being used in a program

# ----- Constants -----
COFFEE_PRICE = 3.50
MUFFIN_PRICE = 2.25
FREE_DRINK_THRESHOLD = 10.00   # spend at least this much to get 1 coffee free

# ----- Input -----
print("Welcome to Campus Café!")
qty_coffee = int(input("How many coffees? "))
qty_muffin = int(input("How many muffins? "))

# ----- Subtotal -----
subtotal = qty_coffee * COFFEE_PRICE + qty_muffin * MUFFIN_PRICE

# ----- Apply free coffee rule -----
free_coffees = 0
if subtotal >= FREE_DRINK_THRESHOLD and qty_coffee > 0:
    free_coffees = 1

# Reduce charge for the free coffee (if any)
coffee_charge_qty = max(qty_coffee - free_coffees, 0)
total = coffee_charge_qty * COFFEE_PRICE + qty_muffin * MUFFIN_PRICE

# ----- Output -----
# NOTE: The print statements here use something called f-strings which
# we will cover next week.
print("\n--- Order Summary ---")
print(f"Coffees: {qty_coffee} (free: {free_coffees})")
print(f"Muffins: {qty_muffin}")
print(f"Subtotal before freebie: ${subtotal:.2f}")
print(f"Total after freebie:     ${total:.2f}")