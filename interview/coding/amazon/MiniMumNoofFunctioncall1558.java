package amazon;

public class MiniMumNoofFunctioncall1558 {
    public int minOperations(int[] target) {
        int operations = 0;
        int maxDoubleOps = 0;

        // Loop through each number in the target array
        for (int num : target) {
            int doubleOps = 0;

            // Process the number until it becomes 0
            while (num > 0) {
                // If the number is odd, subtract 1 (this is an increment operation)
                if (num % 2 == 1) {
                    num--;
                    operations++; // Increment operation
                }
                // If the number is even, divide by 2 (this is a reverse doubling)
                if (num > 0) {
                    num /= 2;
                    doubleOps++; // Doubling operation
                }
            }

            // Track the maximum number of doubling operations needed
            maxDoubleOps = Math.max(maxDoubleOps, doubleOps);
        }

        // Total operations = sum of all increment operations + maximum number of doubling operations
        return operations + maxDoubleOps;
    }
}
