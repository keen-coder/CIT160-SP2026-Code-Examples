# ------------------------------------------------------------------------------
# F-strings can even be used to format floating-point values as percentages
#
# Use the percent sign in the format specifier
# ------------------------------------------------------------------------------

discount = 0.5

# NOTE: the use of the percent sign in the format specifier.
print(f'{discount:%}')

# You can even round to 0 decimal places and display as a percentage
print(f'{discount:.0%}')