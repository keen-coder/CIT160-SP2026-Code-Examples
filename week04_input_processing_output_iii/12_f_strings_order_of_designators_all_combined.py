# ------------------------------------------------------------------------------
# The order in which you list the designators is important!
#
# SYNTAX: {value:[alignment][[0]width][,][.precision][type]}
# ------------------------------------------------------------------------------

# Center-align a float, width of 20, round to two decimal places, group with commas

number = 123456.7890
print(f'|{number:^20,.2f}|')