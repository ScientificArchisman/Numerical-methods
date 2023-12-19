from typing import List, Union

def insertion_sort(arr:List[Union[float, int]]) -> List:
    """ Sort an array using insertion sort algorithm
    Args:
        arr (List[Union[float, int]]): Input array
    Returns:
        List: Sorted array"""  
    # Iterate through the array starting from the second element
    for outer_idx in range(1, len(arr)):
        # Store the current element in a variable
        current = arr[outer_idx]
        # Iterate through the sorted part of the array
        inner_idx = outer_idx-1
        while inner_idx >= 0 and current < arr[inner_idx]:  # Find the position to insert
            arr[inner_idx + 1] = arr[inner_idx]  # Shift element to the right
            inner_idx -= 1
        arr[inner_idx + 1] = current  # Insert the element
    return arr