# Implement the merge sort function merge_sort(Arr,start,end) below
# It should not return anything but sort Arr by the end of the execution.

def merge_sort(arr, start, end):
    """
    Sorts an array from a given start to a given end in ascending order.
    :param arr: an array
    :param start: an index less than end
    :param end: an index greater than start
    :return: None
    """
    if start < end:
        mid = (start + end)//2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid+1, end)
        merge(arr, start, mid, end)

def merge(arr, start, mid, end):
    """
    Merges subarray from start to mid and from mid+1 to end back together in sorted order.
    """
    # temporary arrays to copy elements into subarray
    left_array = [0] * ((mid - start) + 1)
    right_array = [0] * (end - mid)
    for i in range(0, (mid - start) + 1):
        left_array[i] = arr[start + i]
    for i in range(0, end - mid):
        right_array[i] = arr[mid+1+i]

    i, j, k = 0, 0, start

    while i < ((mid - start) + 1) and j < (end - mid):
        # fill the original array with the smallest element (n-1 comparisons at worst)
        if left_array[i] < right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1

    while i < ((mid - start) + 1):
        arr[k] = left_array[i]
        i += 1
        k += 1

    while j < (end - mid):
        arr[k] = right_array[j]
        j += 1
        k += 1

if __name__ == '__main__':
  Arr = [2,14,1,9,10,5,6,18,11]
  merge_sort(Arr, 0, 8)
  print(Arr)