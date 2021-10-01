#Pythagorean Theorem

import math

def pythag():
    a = int(input("What's your value of a?: "))
    b = int(input("What's your value of b?: "))
    cS = a**2 + b**2 
    c = f"c = {int(math.sqrt(cS))}"
    return c

print(pythag())

