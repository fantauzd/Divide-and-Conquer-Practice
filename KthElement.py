# Dominic Fantauzzo
# fantauzd
# 4/16/2024

def kthElement(Arr1, Arr2, k):
    """
    Given two sorted arrays, Arr1 and Arr2 respectively,
    finds the element that would be at the kth position in a combined sorted array.
    :param Arr1: a sorted array
    :param Arr2: a sorted array
    :param k: an index in the combined array
    :return: the element at the kth position or an error message if k is out of range
    """
    # ensure that the desired index is valid
    if k > len(Arr1) + len(Arr2):
        return "Index out of range"
    # use k-1 because we do not want the kth index but the kth position which is at index k-1
    return kth_helper(Arr1, 0, Arr2, 0, k-1)

def kth_helper(Arr1, i, Arr2, j, k):
    """
    A helper function for kthElement()
    :param i: the first index being considered in Arr1
    :param j: the first index being considered in Arr2
    """
    # when we reach base case, return element at kth position
    if k == 0:
        # if we reached the end of an array, the next element comes from remaining array
        if j >= len(Arr2):
            return Arr1[i]
        if i >= len(Arr1):
            return Arr2[j]
        # otherwise return next smallest element
        if Arr1[i] > Arr2[j]:
            return Arr2[j]
        return Arr1[i]
    # if we reached the end of an array, we examine a subarray of the remaining array
    if j >= len(Arr2):
        return kth_helper(Arr1, i+1, Arr2, j, k-1)
    if i >= len(Arr1):
        return kth_helper(Arr1, i, Arr2, j+1, k-1)
    if Arr1[i] > Arr2[j]:
        return kth_helper(Arr1, i, Arr2, j + 1, k - 1)
    return kth_helper(Arr1, i + 1, Arr2, j, k - 1)


if __name__ == '__main__':
  Arr1 = [1,2,3,5,6]
  Arr2= [3,4,5,6,7]
  k= 5
  print(kthElement(Arr1, Arr2, k))

