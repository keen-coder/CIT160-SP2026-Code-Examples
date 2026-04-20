def main():
    # When you call (invoke) a function, Python gives you many options for 
    # passing arguments to that function.

    # Without doing anything extra, Python uses positional arguments, meaning
    # the arguments (actual values) are passed to the parameters in the order
    # that the arguments are listed.

    # If your function does not use default parameter values (discussed later), 
    # then the number of arguments that you pass to the function, must match
    # the exact number of parameters

    # Here I am using positional arguments and since there are 4 parameters, 
    # I must pass in four arguments. Positional arguments are passed to the 
    # parameters from left to right.
    
    result = add(1, 2, 3, 4) # Here 1 is passed to a, 2 to b, 3 to c, 4 to d.

    # Another way to pass arguments is by using 'keyword arguments'. This allows
    # you to explicitly assign an argument value to a specific parameter. It even
    # allows you to pass the arguments in a different order than the parameters
    # are listed.

    # Since add has four parameters and no default values, I must still pass
    # 4 arguments.

    result = add(c=10, b=7, d=44, a=27) # Here 10 is assigned to c, 7 to b, 
                                         # 44 to d and 27 to a


    # It is even possible to use a mix of positional and keyword arguments,
    # BUT the positional arguments must be listed first
    result = add(5, 10, d=15, c=20) # 5 is assigned to a, 10 to b 20 to c and
                                     # 15 to d

    # Now, you can also write your function definitions so that some or all
    # of the parameters are assigned default values (add_with_defaults() below).
    # Basically, if you don't give an argument for that parameter, the default
    # value will be used automatically. This allows you to supply only some of the
    # arguments needed to call the function.

    # The following are examples of using positional arguments with a function
    # that has default values for its paramters
    
    result = add_with_defaults(77)              # a is 77, b is 5, c is 7, d is 42
    result = add_with_defaults(77, 12)          # a is 77, b is 12, c is 7, d is 42
    result = add_with_defaults(77, 12, 32)      # a is 77, b is 12, c is 32, d is 42
    result = add_with_defaults(77, 12, 32, 11)  # a is 77, b is 12, c is 32, d is 11

    # You can also do the same using keyword arguments.
    result = add_with_defaults(c=22)            # a is 1, b is 5, c is 22, d is 42
    result = add_with_defaults(a=12, d=13)      # a is 12, b is 5, c is 7, d is 13

    # And can mix and match (remember positionals still come first)
    result = add_with_defaults(7, 9, d=10)      # a is 7, b is 9, c is 7, d is 10

# Add function with no default parameter values.    
def add(a, b, c, d):
    return a + b + c + d

# Add function with default parameter values.
# NOTE: Not all parameters need a default value, any that don't must always
# be assigned an argument by the function call.
def add_with_defaults(a=1, b=5, c=7, d=42):
    return a + b + c + d







if __name__ == '__main__':
    main()