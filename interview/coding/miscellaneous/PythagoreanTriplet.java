package miscellaneous;

import java.util.Arrays;

public class PythagoreanTriplet {

    public static boolean isPythagoreanTriplet(int[] arr) {
        int n = arr.length;

        // Step 1: Square all elements
        for (int i = 0; i < n; i++) {
            arr[i] = arr[i] * arr[i];
        }

        // Step 2: Sort the squared elements
        Arrays.sort(arr);

        // Step 3: Check for triplets using two-pointer approach
        for (int c = n - 1; c >= 2; c--) {
            int a = 0;
            int b = c - 1;
            while (a < b) {
                if (arr[a] + arr[b] == arr[c]) {
                    return true;
                } else if (arr[a] + arr[b] < arr[c]) {
                    a++;
                } else {
                    b--;
                }
            }
        }

        return false;
    }

    public static void main(String[] args) {
        int[] arr1 = {3, 1, 4, 6, 5};
        System.out.println("Contains Pythagorean triplet: " + isPythagoreanTriplet(arr1)); // Output: true

        int[] arr2 = {10, 4, 6, 12, 5};
        System.out.println("Contains Pythagorean triplet: " + isPythagoreanTriplet(arr2)); // Output: false
    }
}

