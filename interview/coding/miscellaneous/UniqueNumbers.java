package miscellaneous;

public class UniqueNumbers {

    //Find the two non-repeating elements in an array of repeating elements/ Unique Numbers 2

    public static int[] findUniqueNumbers(int[] arr) {
        // Step 1: XOR all elements to get XOR of two unique numbers
        int xorResult = 0;
        for (int num : arr) {
            xorResult ^= num;
        }

        // Step 2: Find a set bit in the xorResult (rightmost set bit)
        int setBit = xorResult & -xorResult;

        // Step 3: Partition the array into two groups and find the unique number in each group
        int num1 = 0, num2 = 0;
        for (int num : arr) {
            if ((num & setBit) != 0) {
                num1 ^= num;
            } else {
                num2 ^= num;
            }
        }

        return new int[]{num1, num2};
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 2, 1, 4};
        int[] result = findUniqueNumbers(arr);

        System.out.println("The two unique numbers are: " + result[0] + " and " + result[1]);
    }
}
