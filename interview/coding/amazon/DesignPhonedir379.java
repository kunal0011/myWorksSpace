package amazon;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;

public class DesignPhonedir379 {
    private Queue<Integer> availableNumbers;
    private HashSet<Integer> inUse;

    /** Initialize your data structure here
     @param maxNumbers - The maximum numbers that can be stored in the phone directory. */
    public DesignPhonedir379(int maxNumbers) {
        availableNumbers = new LinkedList<>();
        inUse = new HashSet<>();

        // Initialize the queue with all available numbers
        for (int i = 0; i < maxNumbers; i++) {
            availableNumbers.offer(i);
        }
    }

    /** Provide a number which is not assigned to anyone.
     @return - Return an available number. Return -1 if none is available. */
    public int get() {
        if (availableNumbers.isEmpty()) {
            return -1;
        }

        int number = availableNumbers.poll();
        inUse.add(number);
        return number;
    }

    /** Check if a number is available or not. */
    public boolean check(int number) {
        return !inUse.contains(number);
    }

    /** Recycle or release a number. */
    public void release(int number) {
        if (inUse.contains(number)) {
            inUse.remove(number);
            availableNumbers.offer(number);
        }
    }

    // Test cases
    public static void main(String[] args) {
        DesignPhonedir379 phoneDirectory = new DesignPhonedir379(3);
        System.out.println(phoneDirectory.get());    // It returns 0
        System.out.println(phoneDirectory.get());    // It returns 1
        System.out.println(phoneDirectory.check(2)); // It returns True, as 2 is available
        System.out.println(phoneDirectory.get());    // It returns 2
        System.out.println(phoneDirectory.check(2)); // It returns False, as 2 is not available
        phoneDirectory.release(2);
        System.out.println(phoneDirectory.check(2)); // It returns True, as 2 is available again
    }
}
