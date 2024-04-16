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
    if k >= Arr1.length() + Arr2.length():
        return "Index out of range"
    return kth_helper(Arr1, 0, Arr2, 0, k)

def kth_helper(Arr1, i, Arr2, j, k):
    """
    A helper function for kthElement()
    :param i: the first index being considered in Arr1
    :param j: the first index being considered in Arr2
    """
