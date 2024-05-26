package miscellaneous;

public class MaximizeExpression {
// Maximize value of (arr[i] – i) – (arr[j] – j) in an array
    public static int maximizeExpression(int[] arr) {
        int n = arr.length;

        if (n < 2) {
            throw new IllegalArgumentException("Array must have at least two elements");
        }

        // Initialize the max and min values of arr[i] - i
        int maxValue = arr[0] - 0;
        int minValue = arr[0] - 0;

        // Traverse the array to find the max and min values of arr[i] - i
        for (int i = 1; i < n; i++) {
            int value = arr[i] - i;
            if (value > maxValue) {
                maxValue = value;
            }
            if (value < minValue) {
                minValue = value;
            }
        }

        // The result is the difference between the max and min values
        return maxValue - minValue;
    }

    public static void main(String[] args) {
        int[] arr = {10, 3, 1, 8, 5, 12};
        System.out.println("Maximum value of (arr[i] - i) - (arr[j] - j): " + maximizeExpression(arr));
    }
}
