# Question: Merge Sort Implementation
# Please DO NOT modify the given function except the TODO part
# You may have your own functions if necessary

def merge_sort(arr):
    """
    Implement the merge sort algorithm to sort an array in ascending order.
    
    The merge sort algorithm uses the divide-and-conquer strategy:
    1. Divide the input array into two halves
    2. Recursively sort the two halves
    3. Merge the sorted halves to produce the final sorted array
    
    :param arr: A list of comparable elements
    :return: A new sorted list containing the same elements as arr
    """
    # TODO: Implement merge sort algorithm

    if len(arr) == 1:
        return arr
    else:
        div = len(arr) // 2
        left = merge_sort(arr[: div])
        right = merge_sort(arr[div: ])
        i = j = 0
        res = []
        while j <= len(right) - 1 and i <= len(left) - 1:
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res = res + left[i: ]
        res = res + right[j: ]
        return res


# Example usage
if __name__ == '__main__':
    test_array = [64, 34, 25, 12, 22, 11, 90]
    
    # Students should complete the implementation and test the method
    # sorted_array = merge_sort(test_array)
    # print("Original array:", test_array)
    # print("Sorted array:", sorted_array)