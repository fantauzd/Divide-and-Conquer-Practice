# Dominic Fantauzzo

# Double the value of each element in a given array using divide and conquer (no iteration)
def foo(arr, start, end):
    """
    Doubles the value of each element in the array from start to end.
    :param arr: An array of integers
    :param start: An index less than end
    :param end: An index greater than start
    :return: None
    """
    if start < end:
        mid = (start + end) // 2
        # divide the array into two parts
        foo(arr, start, mid)
        foo(arr, mid+1, end)
    # at the base case, solve the subproblem
    else:
        arr[start] = 2 * arr[start]



if __name__ == '__main__':
  arr = [1,2,3,4,5,6,7]
  foo(arr, 0, 6)

  for i in range(0, 7):
    print(arr[i])