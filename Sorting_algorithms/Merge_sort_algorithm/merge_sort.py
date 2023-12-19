from typing import List, Union
def join_two_sorted_arrays(arr1: List[Union[int, float]], arr2: List[Union[int, float]],
                            final_array: List[Union[int, float]]) -> None:
    """Join two sorted arrays into one sorted array
    Args:
        arr1 (List[Union[int, float]]): The first sorted array
        arr2 (List[Union[int, float]]): The second sorted array
        final_array (List[Union[int, float]], optional): The final sorted array.
    Returns:
        None: The final sorted array is stored in final_array"""
    pointer1, pointer2, pointer3 = 0, 0, 0 # pointers to the first element of each array
    while pointer1 < len(arr1) and pointer2 < len(arr2):
        if arr1[pointer1] < arr2[pointer2]:
            final_array[pointer3] = arr1[pointer1]
            pointer1 += 1
            pointer3 += 1
        else:
            final_array[pointer3] = arr2[pointer2]
            pointer2 += 1
            pointer3 += 1
    # Add the remaining elements of the first array
    while pointer1 < len(arr1):
        final_array[pointer3] = arr1[pointer1]
        pointer1 += 1
        pointer3 += 1

    # Add the remaining elements of the second array
    while pointer2 < len(arr2):
        final_array[pointer3] = arr2[pointer2]
        pointer2 += 1
        pointer3 += 1

def merge_sort(arr: List[Union[int, float]]) -> List[Union[int, float]]:
    """Sort an array using mergesort algorithm
    Args:
        arr (List[Union[int, float]]): The array to be sorted
    Returns:
        (List[Union[int, float]]): The sorted array"""
    if len(arr) <= 1: return  # Base case
    # Split the array into two halves
    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]

    # Sort the two halves
    merge_sort(left)
    merge_sort(right)

    # Join the two halves
    join_two_sorted_arrays(left, right, arr)

# Driver code

if __name__ == "__main__":
    arr = [5, 2, 1, 3, 6, 4]
    merge_sort(arr)
    print(arr)