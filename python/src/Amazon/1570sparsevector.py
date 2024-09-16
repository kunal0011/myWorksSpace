class SparseVector:
    def __init__(self, nums):
        # Store non-zero elements and their indices
        self.non_zero = {i: num for i, num in enumerate(nums) if num != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        result = 0
        # Iterate over the non-zero elements of this vector
        for i, val in self.non_zero.items():
            if i in vec.non_zero:
                result += val * vec.non_zero[i]
        return result


# Testing
v1 = SparseVector([1, 0, 0, 2, 3])
v2 = SparseVector([0, 3, 0, 4, 0])
print("Python Test Result:", v1.dotProduct(v2))  # Output should be 8
