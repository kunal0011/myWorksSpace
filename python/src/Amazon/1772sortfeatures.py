class Solution:
    def sortFeatures(self, features: list[str], responses: list[str]) -> list[str]:
        # Create a dictionary to store the count of each feature
        feature_count = {feature: 0 for feature in features}

        # Count the occurrences of each feature in the responses
        for response in responses:
            # Use a set to avoid counting duplicates in the same response
            words = set(response.lower().split())
            for feature in features:
                if feature in words:
                    feature_count[feature] += 1

        # Sort the features by their count (in descending order)
        # If counts are the same, maintain the original order from the input
        return sorted(features, key=lambda x: (-feature_count[x], features.index(x)))


# Testing the solution
if __name__ == "__main__":
    solution = Solution()

    # Test case
    features = ["cooler", "lock", "touch"]
    responses = ["i like cooler cooler", "lock touch cool", "locker room"]
    # Expected output: ["cooler", "touch", "lock"]
    print("Sorted features:", solution.sortFeatures(features, responses))

# Problem Breakdown:
# Features: A list of keywords representing product features.
# Responses: A list of customer feedback strings, where each string may contain multiple words, including features.
# Task: You need to count the occurrences of each feature in the responses (case-insensitive) and return the features sorted by their frequency. If two features have the same frequency, they should appear in the order they were given in the original feature list.
