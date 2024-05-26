package miscellaneous;

import java.util.*;

public class FindPairsWithSum {

    public static List<List<Integer>> findPairs(int[] arr1, int[] arr2, int targetSum) {
        Set<Integer> set = new HashSet<>();
        List<List<Integer>> result = new ArrayList<>();

        // Add elements of arr1 to the set
        for (int num : arr1) {
            set.add(num);
        }

        // Iterate through arr2 to find pairs
        for (int num : arr2) {
            if (set.contains(targetSum - num)) {
                List<Integer> pair = new ArrayList<>();
                pair.add(targetSum - num);
                pair.add(num);
                result.add(pair);
            }
        }

        return result;
    }

    public static void main(String[] args) {
        int[] arr1 = {1, 2, 4, 5, 7};
        int[] arr2 = {5, 6, 3, 4, 8};
        int targetSum = 9;

        List<List<Integer>> pairs = findPairs(arr1, arr2, targetSum);

        System.out.println("Pairs with sum " + targetSum + ":");
        for (List<Integer> pair : pairs) {
            System.out.println(pair.get(0) + ", " + pair.get(1));
        }
    }
}

