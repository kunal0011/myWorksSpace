def distinctNumbersInEachSubarray(arr: list[int], k: int) -> list[int]:
    n = len(arr)
    if k > n:
        return []

    # Dictionary to keep track of the count of each number in the current window
    freq_map = {}
    result = []

    # Initialize the frequency map with the first window
    for i in range(k):
        freq_map[arr[i]] = freq_map.get(arr[i], 0) + 1

    # Add the count of distinct numbers in the first window
    result.append(len(freq_map))

    # Slide the window through the array
    for i in range(k, n):
        # Remove the element going out of the window
        out_elem = arr[i - k]
        freq_map[out_elem] -= 1
        if freq_map[out_elem] == 0:
            del freq_map[out_elem]

        # Add the new element coming into the window
        in_elem = arr[i]
        freq_map[in_elem] = freq_map.get(in_elem, 0) + 1

        # Add the count of distinct numbers in the current window
        result.append(len(freq_map))

    return result


# Example usage:
arr1 = [1, 2, 1, 3, 4, 2, 3]
k1 = 4
print(distinctNumbersInEachSubarray(arr1, k1))  # Output: [3, 4, 4, 3]

arr2 = [4, 1, 1, 2, 3, 3, 1]
k2 = 3
print(distinctNumbersInEachSubarray(arr2, k2))  # Output: [2, 2, 3, 2, 2]
