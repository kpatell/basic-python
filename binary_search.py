"""Classic binary search algorithm"""


def binary_search(array, low, high, element) -> int:
    """Binary search algorithm that returns the index of the element to look for"""
    if high >= low:
        mid = int((high + low) / 2)

        if array[mid] == element:
            return mid
        elif array[mid] > element:
            return binary_search(array, mid + 1, high, element)
        else:
            return binary_search(array, low, mid - 1, element)
    else:
        return -1  # element not in array


arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(arr, end="\n\n")
print("What element index to find?: ", end="")
element = int(input())

print("The element", element, "is at index",
      binary_search(arr, 0, len(arr) - 1, element))
