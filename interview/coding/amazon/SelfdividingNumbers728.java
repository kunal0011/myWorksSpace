package amazon;

import java.util.ArrayList;
import java.util.List;

public class SelfdividingNumbers728 {
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> result = new ArrayList<>();

        for (int num = left; num <= right; num++) {
            if (isSelfDividing(num)) {
                result.add(num);
            }
        }

        return result;
    }

    private boolean isSelfDividing(int n) {
        int original = n;
        while (n > 0) {
            int digit = n % 10;
            if (digit == 0 || original % digit != 0) {
                return false;
            }
            n /= 10;
        }
        return true;
    }

    // Test the function
    public static void main(String[] args) {
        SelfdividingNumbers728 sol = new SelfdividingNumbers728();

        // Test case 1
        int left_1 = 1, right_1 = 22;
        System.out.println(sol.selfDividingNumbers(left_1, right_1));  // Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

        // Test case 2
        int left_2 = 47, right_2 = 85;
        System.out.println(sol.selfDividingNumbers(left_2, right_2));  // Output: [48, 55, 66, 77]
    }
}
