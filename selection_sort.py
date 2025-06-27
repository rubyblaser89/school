#!/usr/bin/python3

def selection_sort(arr):

    n = len(arr)

    for i in range(n):

# Find the minimum element in the unsorted portion

        min_idx = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_idx]:

                min_idx = j

# Swap the found minimum element with the first element of the unsorted portion
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

my_list = list(input("Please Input Array to Sort: "))

selection_sort(my_list)

print(f"Sorted array: {my_list}")