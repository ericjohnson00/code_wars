"""
    
    These are my notes and solutions for codewars
    
    
"""
# You Can't Code Under Pressure #1
# Code as fast as you can! You need to double the integer and return it.

def double_integer(i):
    return i * 2
    

# Binary Addition
# Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.
# The binary number returned should be a string.
# Examples:(Input1, Input2 --> Output (explanation)))

def add_binary(a,b):
    sum = a + b
    return bin(sum)[2:]
    
    
print(add_binary(1, 3))



# Opposites Attract
# Timmy & Sarah think they are in love, but around where they live, 
# they will only know once they pick a flower each. If one of the flowers 
# has an even number of petals and the other has an odd number of petals
# it means they are in love.
# Write a function that will take the number of petals of each flower and 
# return true if they are in love and false if they aren't.

def lovefunc( flower1, flower2 ):
    if (flower1 % 2 == 0 and flower2 % 2 != 0) or (flower1 % 2 != 0 and flower2 % 2 == 0):
        return True
    else:
        return False
    
print(lovefunc(3, 5))

# another exampke
# def lovefunc(flower1, flower2):
#     return flower1 % 2 != flower2 % 2




# Sum of odd numbers
# Given the triangle of consecutive odd numbers:
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

# 1 -->  1
# 2 --> 3 + 5 = 8

def row_sum_odd_numbers(n):
    return n**3


# Growth of a Population
# In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. How many years does the town need to see its population greater than or equal to p = 1200 inhabitants?

# At the end of the first year there will be: 
# 1000 + 1000 * 0.02 + 50 => 1070 inhabitants

# At the end of the 2nd year there will be: 
# 1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an integer **)

# At the end of the 3rd year there will be:
# 1141 + 1141 * 0.02 + 50 => 1213

# It will need 3 entire years.
# More generally given parameters:

# p0, percent, aug (inhabitants coming or leaving each year), p (population to equal or surpass)

# the function nb_year should return n number of entire years needed to get a population greater or equal to p.

# aug is an integer, percent a positive or null floating number, p0 and p are positive integers (> 0)

# Examples:
# nb_year(1500, 5, 100, 5000) -> 15
# nb_year(1500000, 2.5, 10000, 2000000) -> 10
# Note:
# Don't forget to convert the percent parameter as a percentage in the body of your function: if the parameter percent is 2 you have to convert it to 0.02.

# There are no fractions of people. At the end of each year, the population count is an integer: 252.8 people round down to 252 persons.



def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
        p0 += int(p0 * (percent / 100)) + aug  # Apply growth and fixed increase
        years += 1  # Count the year
    return years




# Abbreviate a Two Word Name
# Description:
# Write a function to convert a name into initials. This kata strictly 
# takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:

# Sam Harris => S.H

# patrick feeney => P.F


def abbrev_name(name):
    first, last = name.split()
    return f"{first[0].upper()}.{last[0].upper()}"
    
print(abbrev_name("Eric Johnson"))


# Convert a Boolean to a String
# Implement a function which convert the given boolean value into its string representation.

# Note: Only valid inputs will be given.

def boolean_to_string(b):
    if b:
        return 'True'
    else:
        return 'False'
    
print(boolean_to_string(True))




# Grasshopper - Summation
# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0. Your function only needs to return the result, what is shown between parentheses in the example below is how you reach that result and it's not part of it, see the sample tests.

# For example (Input -> Output):

# 2 -> 3 (1 + 2)
# 8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)

def summation(num):
    return sum(range(num + 1))

print(summation(8))



# Sort the odd
# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]


def sort_array(source_array):
    odds = sorted((x for x in source_array if x % 2 != 0), reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in source_array]

print(sort_array([5, 3, 2, 8, 1, 4]))

# another example
# def sort_array(source_array):
#     odds = sorted((x for x in source_array if x % 2 != 0), reverse=True)
#     return [x if x % 2 == 0 else odds.pop(0) for x in source_array]

