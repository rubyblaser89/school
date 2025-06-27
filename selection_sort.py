#!/usr/bin/python3

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Find the minimum element in the unsorted part of the array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Get user input
array = input("Please Enter Array to Sort (e.g. 5 4 3 2 1): ")

# Convert input string to a list of numbers
try:
    numbers = [int(a) for a in array.split()]
except ValueError:
    print("Invalid input. No Numbers Entered.")

else:
    print("Original list:", numbers)
    sorted_numbers = selection_sort(numbers)
    print("Sorted list (Selection Sort):", sorted_numbers)
