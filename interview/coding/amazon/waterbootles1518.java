package amazon;

public class waterbootles1518 {
    public int numWaterBottles(int numBottles, int numExchange) {
        int totalDrinks = numBottles;
        int emptyBottles = numBottles;

        while (emptyBottles >= numExchange) {
            // How many new full bottles we can get from empty ones
            int newBottles = emptyBottles / numExchange;
            totalDrinks += newBottles;

            // Update the number of empty bottles
            emptyBottles = newBottles + (emptyBottles % numExchange);
        }

        return totalDrinks;
    }

    // Testing
    public static void main(String[] args) {
        waterbootles1518 solution = new waterbootles1518();
        int numBottles = 9;
        int numExchange = 3;
        System.out.println("Java Test Result: " + solution.numWaterBottles(numBottles, numExchange));  // Output should be 13
    }
}

