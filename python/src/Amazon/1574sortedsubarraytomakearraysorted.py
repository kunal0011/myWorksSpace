def findLengthOfShortestSubarray(arr):
    n = len(arr)
    left = 0

    # Step 1: Find the longest sorted prefix
    while left < n - 1 and arr[left] <= arr[left + 1]:
        left += 1

    # If fully sorted, return 0
    if left == n - 1:
        return 0

    right = n - 1

    # Step 2: Find the longest sorted suffix
    while right > left and arr[right] >= arr[right - 1]:
        right -= 1

    # Step 3: Initialize minimum length to remove either prefix or suffix
    min_length = min(n - left - 1, right)

    # Step 4: Check combinations of removing elements from both sides
    for i in range(left + 1):
        while right < n and arr[i] > arr[right]:
            right += 1
        min_length = min(min_length, right - i - 1)

    return min_length


# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 3, 10, 4, 2, 3, 5]
    print(findLengthOfShortestSubarray(arr))  # Output: 5
