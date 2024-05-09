import math
import sys

def log_cal():
    list_len = input("Length: ")
    return math.log(int(list_len)*2)

print(f"{log_cal():.0f}")

print(math.factorial(int(sys.argv[1])))