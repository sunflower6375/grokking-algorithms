#recursion is when a function calls itself
#every recursive function has 2 parts: the base case & the recursive case
#so the function doesnt go into an infinite loop

# def countdown(i):
#     print(i)
#     if i <= 0:
#         return
#     else:
#         countdown(i-1)

# print(countdown(3))
import math

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
print(fact(6))

print(math.factorial(6))