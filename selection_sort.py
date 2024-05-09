#sorting an array from smallest to largest

def findSmallest(arr):
    smallest = arr[0] #stores the smallest value
    smallest_index = 0 #stores index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

#writing selection sort function from find smallest function:
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))