from typing import List, Union

def selection_sort(array : List[Union[int, float]]) -> List[Union[int, float]]:
    """Sorts an array in ascending order with selection sort
    Args:
        array(List[Union[int, float]]) : The array to be sorted in ascending order
    Returns:
        (List[Union[int, float]]) : the sorted array"""
    for passNum in range(len(array) - 1, 0, -1):
        max_idx: int = 0 # index of the maximum value
        # Find the index of the maximum value
        for idx in range(passNum + 1):
            if array[idx] > array[max_idx]:
                max_idx: int = idx
        # Swap maximum value to its correct position 
        array[max_idx], array[passNum] = array[passNum], array[max_idx]
    return array