package miscellaneous;

public class HighestPowerOfTwo {

    public static int highestPowerOfTwo(int n) {
        if (n <= 1) {
            return 0; // There is no power of 2 less than or equal to 1
        }

        int low = 0;
        int high = n;
        int result = 0;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            int pow = (int) Math.pow(2, mid);

            if (pow <= n) {
                result = pow;
                low = mid + 1; // Update the lower bound
            } else {
                high = mid - 1; // Update the upper bound
            }
        }

        return result;
    }

    public static void main(String[] args) {
        int number = 25;
        System.out.println("Highest power of 2 less than or equal to " + number + ": " + highestPowerOfTwo(number)); // Output: 16
    }
}
