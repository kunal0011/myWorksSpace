package searching_sorting;

import java.util.Arrays;
import java.util.Comparator;

public class LargestNumber {
    public static String largestNumber(int[] nums) {
        // Convert the integers to strings
        String[] strs = Arrays.stream(nums)
                .mapToObj(String::valueOf)
                .toArray(String[]::new);

        // Sort the strings based on the custom comparator
        Arrays.sort(strs, (s1, s2) -> (s2 + s1).compareTo(s1 + s2));

        // If the largest number is "0", return "0"
        if (strs[0].equals("0")) {
            return "0";
        }

        // Join the sorted strings to form the largest number
        return String.join("", strs);
    }

    public static void main(String[] args) {
        int[] nums = {3, 30, 34, 5, 9};
        System.out.println("Largest number: " + largestNumber(nums)); // Output: 9534330
    }
}
