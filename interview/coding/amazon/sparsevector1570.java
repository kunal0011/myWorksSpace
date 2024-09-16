package amazon;

import java.util.HashMap;
import java.util.Map;

public class sparsevector1570 {
    private Map<Integer, Integer> nonZero;

    // Constructor to store non-zero elements
    sparsevector1570(int[] nums) {
        nonZero = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                nonZero.put(i, nums[i]);
            }
        }
    }

    // Return the dotProduct of two sparse vectors
    public int dotProduct(sparsevector1570 vec) {
        int result = 0;
        // Iterate over the non-zero elements of this vector
        for (Map.Entry<Integer, Integer> entry : nonZero.entrySet()) {
            int index = entry.getKey();
            int value = entry.getValue();
            if (vec.nonZero.containsKey(index)) {
                result += value * vec.nonZero.get(index);
            }
        }
        return result;
    }

    // Testing
    public static void main(String[] args) {
        sparsevector1570 v1 = new sparsevector1570(new int[]{1, 0, 0, 2, 3});
        sparsevector1570 v2 = new sparsevector1570(new int[]{0, 3, 0, 4, 0});
        System.out.println("Java Test Result: " + v1.dotProduct(v2));  // Output should be 8
    }
}

