"""
    In order to avoid confusion and to ensure that everyone always
    arrives at the same result, mathematicians established a standard 
    order of operations for calculations that involve more than one arithmetic 
    operation. Arithmetic operations should always be carried out in the 
    following order:

    Simplify the expressions inside parentheses ( ), brackets [ ], braces { } and fractions bars.
    Evaluate all powers.
    Do all multiplications and divisions from left to right.
    Do all additions and subtractions from left to right.


"""

list = ["cum", "piss", "hole", 6, 3, 9]

sorted = sorted(list, key = str)
print(sorted)