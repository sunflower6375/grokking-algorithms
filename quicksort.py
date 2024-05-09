#divide and conquer is a well known recursive technique used to solve problems
from time import sleep

def quicksort(array):
    if len(array) < 2:
        return array #base case
    else: 
        pivot= array[0] #recursive case
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot]+ quicksort(greater)

print(quicksort([10, 5, 2, 3]))

def print_items2(list):
    for item in list:
        sleep(1)
        print(item)
print(print_items2)