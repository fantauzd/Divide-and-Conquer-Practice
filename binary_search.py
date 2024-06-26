# Search for an element in a list of sorted numbers using Divide and Conquer Technique.
# If the element is found return the index of the key, else return -1.

def search(numArr, key):
    """
    Search for an element in an array of sorted numbers
    :param numArr: an array of sorted numbers
    :param key: number
    :return: index if key is found, else -1
    """
    return search_helper(numArr, 0, len(numArr) - 1, key)


def search_helper(numArr, start, end, key):
    """
    search helper function.
    """
    if start <= end:
        mid = (end + start) // 2
        if numArr[mid] == key:
            return mid

        if numArr[mid] > key:
            return search_helper(numArr, start, mid-1, key)

        if numArr[mid] < key:
            return search_helper(numArr, mid+1, end, key)

    return -1

if __name__ == '__main__':
  a = [1,3,4,5,6,7,8,9]
  result = search(a, 9)
  print(result)