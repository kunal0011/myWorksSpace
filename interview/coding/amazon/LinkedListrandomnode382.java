package amazon;

import java.util.Random;

class ListNode382 {
    int val;
    ListNode382 next;
    ListNode382(int val) { this.val = val; }
}

public class LinkedListrandomnode382 {
    private ListNode382 head;
    private Random random;

    public LinkedListrandomnode382(ListNode382 head) {
        this.head = head;
        this.random = new Random();
    }

    public int getRandom() {
        ListNode382 current = head;
        int result = current.val;
        int count = 1;

        // Traverse the linked list
        while (current != null) {
            // Pick the current node with probability 1/count
            if (random.nextInt(count) == 0) {
                result = current.val;
            }
            current = current.next;
            count++;
        }

        return result;
    }

    // Test cases
    public static void main(String[] args) {
        // Create linked list: 1 -> 2 -> 3
        ListNode382 head = new ListNode382(1);
        head.next = new ListNode382(2);
        head.next.next = new ListNode382(3);

        // Initialize solution
        LinkedListrandomnode382 solution = new LinkedListrandomnode382(head);

        // Call getRandom multiple times to see random behavior
        for (int i = 0; i < 5; i++) {
            System.out.println(solution.getRandom());  // Should randomly print 1, 2, or 3 each time
        }
    }
}
