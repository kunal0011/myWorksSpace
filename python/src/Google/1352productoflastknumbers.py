class ProductOfNumbers:

    def __init__(self):
        self.prefix_products = [1]  # Start with a dummy product of 1

    def add(self, num: int) -> None:
        if num == 0:
            # Reset if a zero is added
            self.prefix_products = [1]
        else:
            # Multiply the last prefix product by the new number
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix_products):
            return 0  # If k is larger than or equal to the length of prefix_products, a zero was included
        return self.prefix_products[-1] // self.prefix_products[-k-1]
