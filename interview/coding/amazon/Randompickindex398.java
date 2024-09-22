package amazon;

import java.util.*;

public class Randompickindex398 {
    private Map<Integer, List<Integer>> indices;

    public Randompickindex398(int[] nums) {
        indices = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            indices.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        }
    }

    public int pick(int target) {
        if (indices.containsKey(target)) {
            List<Integer> list = indices.get(target);
            Random rand = new Random();
            return list.get(rand.nextInt(list.size()));
        }
        return -1;
    }

    // Example usage
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 3, 3};
        Randompickindex398 randomPicker = new Randompickindex398(nums);
        System.out.println(randomPicker.pick(3));  // Randomly output one of the indices 2, 3, or 4
        System.out.println(randomPicker.pick(1));  // Output: 0
        System.out.println(randomPicker.pick(4));  // Output: -1 (not found)
    }
}
