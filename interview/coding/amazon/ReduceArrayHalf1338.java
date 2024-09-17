package amazon;

import java.util.*;

public class ReduceArrayHalf1338 {
    public int minSetSize(int[] arr) {
        // Step 1: Count the frequency of each element
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : arr) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        // Step 2: Sort the frequencies in descending order
        List<Integer> freqValues = new ArrayList<>(freq.values());
        Collections.sort(freqValues, Collections.reverseOrder());

        // Step 3: Remove elements by frequency until at least half are removed
        int halfSize = arr.length / 2;
        int removed = 0, setSize = 0;

        for (int count : freqValues) {
            removed += count;
            setSize++;
            if (removed >= halfSize) {
                break;
            }
        }

        return setSize;
    }

    // Testing
    public static void main(String[] args) {
        ReduceArrayHalf1338 solution = new ReduceArrayHalf1338();
        int[] arr = {3,3,3,3,5,5,5,2,2,7};
        System.out.println("Java Test Result: " + solution.minSetSize(arr));  // Output: 2
    }
}
