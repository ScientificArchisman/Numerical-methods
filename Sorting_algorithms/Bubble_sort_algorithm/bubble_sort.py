from typing import List, Union

def bubble_sort(arr:List[Union[float, int]]) -> List:
    """Sort an array using bubble sort. 
    A modified version of the method is used by implementing a flag
    at each pass. If no swaps are made in a particular pass, we stop 
    the method as the array is already sorted by this point.
    We make the flag True if even one swap is made in a pass
    so that the method doesn't stop.
    Args:
        arr(List[Union[int, float]]) : the array to sort
    Returns:
        The sorted array in place."""
    # We are doing n-1 passes so we count down from n-1 to 1
    for passNum in range(len(arr) - 1, 0, -1):
        swapDone: bool = False # we create a flag counter to stop the cycle of the array is sorted
        for idx in range(passNum):
            if arr[idx] > arr[idx + 1]:
                # If the next position is greater than the initial position , we swap them.
                arr[idx], arr[idx + 1] = arr[idx+1], arr[idx]
                swapDone: bool = True # increase the flag to NOT stop the process
        # if no swaps were made, we stop the process as the array is already sorted at this point.
        if swapDone == False: return arr 
    return arr