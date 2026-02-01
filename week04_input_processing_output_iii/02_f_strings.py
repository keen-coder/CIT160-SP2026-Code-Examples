# ------------------------------------------------------------------------------
# Formatted string literals or f-strings provide many ways to format your output.
# Be sure to read the pdf under this week's readings for even more examples.
#
# f-strings always start with a lowercase f BEFORE the opening quote.
# ------------------------------------------------------------------------------



# f-strings can also be used to format how the output of value looks by adding
# a format-specifier to the place holder.
#
# Syntax: {placeholder:format-specifier}
# Order of designators: [[fill][alignment][width]][,][.precision][type]

# ALIGNMENT & WIDTH
# The following characters can be used to change the alignment of the output 
# given a width:
#   <   left-align
#   >   right-align
#   ^   center-align
# If the number of characters in the output is smaller than the width, 
# spaces will be used to fill in the missing characters. 
# You can also change the filler character to something other than spaces.

print(f'{'ALIGNMENT':=^80}')
PI = 3.141592653589793
print(f'|{PI:25}|') # No Alignment (Default is Right-Align)
print(f'|{PI:<25}|') # Left-Align
print(f'|{PI:>25}|') # Right-Align
print(f'|{PI:^25}|') # Center-Align

print()

# You can specify a fill character to use instead of spaces.
name = 'Carol'
print(f'|{name:+<25}|') # Left-Align
print(f'|{name:+>25}|') # Right-Align
print(f'|{name:+^25}|') # Center-Align

print('='*80) # Print a number of = to separate the output
print()

print(f'{'FORMATTING FLOATS':=^80}')

# f-strings can format floating point values, specifically how many
# decimal place should be displayed / rounded to. 
# The character f is used (indepednat of the 'f' at the beginning of the f-string)
# to designate that the value being formatted is a float.
PI = 3.141592653589793