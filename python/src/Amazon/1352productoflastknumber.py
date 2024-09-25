class ProductOfNumbers:

    def __init__(self):
        # Start with 1 as a base product to make multiplication easy
        self.products = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # Reset the products list when a zero is added
            self.products = [1]
        else:
            # Append the new cumulative product
            self.products.append(self.products[-1] * num)

    def getProduct(self, k: int) -> int:
        # If the length of the products list is less than k + 1, it means we encountered a zero
        if len(self.products) <= k:
            return 0
        # Return the product of the last k elements
        return self.products[-1] // self.products[-k-1]
