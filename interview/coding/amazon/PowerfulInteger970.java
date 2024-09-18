package amazon;

import java.util.*;

public class PowerfulInteger970 {
    public List<Integer> powerfulIntegers(int x, int y, int bound) {
        Set<Integer> result = new HashSet<>();

        // Iterate through powers of x
        for (int i = 0; Math.pow(x, i) <= bound; i++) {
            for (int j = 0; Math.pow(y, j) <= bound; j++) {
                int powerfulInt = (int) Math.pow(x, i) + (int) Math.pow(y, j);
                if (powerfulInt <= bound) {
                    result.add(powerfulInt);
                }
                if (y == 1) break;  // Stop if y is 1 to avoid infinite loop
            }
            if (x == 1) break;  // Stop if x is 1 to avoid infinite loop
        }

        return new ArrayList<>(result);
    }

    // Testing
    public static void main(String[] args) {
        PowerfulInteger970 solution = new PowerfulInteger970();
        int x = 2;
        int y = 3;
        int bound = 10;
        System.out.println("Java Test Result: " + solution.powerfulIntegers(x, y, bound));  // Output: [2, 3, 4, 5, 7, 9, 10]
    }
}

