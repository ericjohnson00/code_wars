"""
    
    These re my notes and solutions for codewars
    
    
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