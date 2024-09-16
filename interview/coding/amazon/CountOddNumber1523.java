package amazon;

public class CountOddNumber1523 {
    public int countOdds(int low, int high) {
        // The formula calculates how many odd numbers are between low and high
        return (high + 1) / 2 - low / 2;
    }

    // Testing
    public static void main(String[] args) {
        CountOddNumber1523 solution = new CountOddNumber1523();
        int low = 3;
        int high = 7;
        System.out.println("Java Test Result: " + solution.countOdds(low, high));  // Output should be 3
    }
}

