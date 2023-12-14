from typing import List, Union

def linear_search(arr: List[Union[int, float]], target: Union[int, float]) -> Union[int, None]:
    """ Return the index of the target in an unsorted array with linear search
    If the target is not in the array, return None
    Args:
        arr (list[int, float]): an unsorted array of integers
        target (int or float): the target integer
    Returns:
        the index of the target in the array if present else None
    """
    for idx, val in enumerate(arr):
        if val == target: # If the value is the target, return the index
            return idx
    return None


def binary_search(arr: List[Union[int, float]], target: Union[int, float]) -> Union[int, None]:
    """Return the index of the target in a sorted array with binary search
    If the target is not in the array, return None
    Args:
        arr (list(int, float)): a sorted array of integers
        target (int or float): the target integer
    Returns:
        the index of the target in the array if present, else None
    """
    low_idx, high_idx = 0, len(arr) - 1  # Use 2 pointers to track the range of the target
    while low_idx <= high_idx:
        mid_idx : int = (low_idx + high_idx) // 2 # Find the middle index
        mid_val : Union[int, float] = arr[mid_idx] # Find the middle value
        if mid_val == target: return mid_idx # If the middle value is the target, return the index
        # If the middle value is less than the target, move the low pointer to the middle index + 1
        elif mid_val < target: low_idx = mid_idx + 1 
        # If the middle value is greater than the target, move the high pointer to the middle index - 1
        else: high_idx = mid_idx - 1
    return None # If the target is not in the array, return None


def interpolation_search(arr: List[Union[int, float]], target: Union[int, float]) -> Union[int, None]:
    """ Return the index of the target in a sorted array with interpolation search
    If the target is not in the array, return None
    Args:
        arr (List[int, float]): a sorted array of integers
        target (int or float): the target integer
    Returns:
        the index of the target in the array
    Calculate the middle index by the linear interpolation formula:
    y = y1 + (y2 - y1) * (x - x1) / (x2 - x1), where y is the element in the array and x is the index
    We need to modify the formula to find x, the index of the target.
    y2, y1 are tarken as the values of the high and low pointers, x2, x1 are taken as the indices of the high and low pointers
    It is  sort of normalizing the formula to find the index of the target
    """
    low_idx, high_idx = 0, len(arr) - 1 # Use 2 pointers to track the range of the target
    while low_idx <= high_idx and target >= arr[low_idx] and target <= arr[high_idx]:
        if low_idx == high_idx:
            if arr[low_idx] == target:
                return low_idx
            else:
                return None
            
        # Safe division by checking for zero
        denom = arr[high_idx] - arr[low_idx]
        if denom == 0:
            break  # Avoid division by zero
            
        mod_min_idx = low_idx + int(((target - arr[low_idx]) / denom) * (high_idx - low_idx))
        # Ensure the index is within the range
        mod_min_idx = max(min(mod_min_idx, high_idx), low_idx)

        if arr[mod_min_idx] == target: return mod_min_idx # If the middle value is the target, return the index
        # If the middle value is less than the target, move the low pointer to the middle index + 1
        elif arr[mod_min_idx] < target: low_idx = mod_min_idx + 1 
        # If the middle value is greater than the target, move the high pointer to the middle index - 1
        else: high_idx = mod_min_idx - 1 
    return None # If the target is not in the array, return None



def search_array(arr: List[Union[int, float]], target: Union[int, float], sorted: bool = False, 
                 method_if_sorted: str = "interpolation") -> Union[int, None]:
    """
    Return the index of the target in an array.
    Args:
        arr (List[Union[int, float]]): An array of integers or floats.
        target (Union[int, float]): The target integer or float.
        sorted (bool): Whether the array is sorted.
        method_if_sorted (str): The method to use if the array is sorted ("binary", "interpolation").
    Returns:
        Union[int, None]: The index of the target in the array, or None if not found.
    """
    if sorted:
        if method_if_sorted == "interpolation":
            return interpolation_search(arr=arr, target=target)
        elif method_if_sorted == "binary":
            return binary_search(arr=arr, target=target)
    return linear_search(arr=arr, target=target)
