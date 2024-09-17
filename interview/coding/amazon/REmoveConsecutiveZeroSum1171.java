package amazon;

import java.util.HashMap;

class ListNode1171 {
    int val;
    ListNode1171 next;
    ListNode1171() {}
    ListNode1171(int val) { this.val = val; }
    ListNode1171(int val, ListNode1171 next) { this.val = val; this.next = next; }
}

public class REmoveConsecutiveZeroSum1171 {
    public ListNode1171 removeZeroSumSublists(ListNode1171 head) {
        ListNode1171 dummy = new ListNode1171(0);  // Dummy node to handle edge cases
        dummy.next = head;

        HashMap<Integer, ListNode1171> prefixMap = new HashMap<>();
        int prefixSum = 0;
        ListNode1171 current = dummy;

        // First pass: record the latest occurrence of each prefix sum
        while (current != null) {
            prefixSum += current.val;
            prefixMap.put(prefixSum, current);
            current = current.next;
        }

        // Second pass: reset the next pointers to remove zero-sum sublists
        prefixSum = 0;
        current = dummy;
        while (current != null) {
            prefixSum += current.val;
            // Skip all nodes in between the first and last occurrence of the same prefix sum
            current.next = prefixMap.get(prefixSum).next;
            current = current.next;
        }

        return dummy.next;
    }

    // Helper function to create a linked list from an array
    public static ListNode1171 createLinkedList(int[] values) {
        ListNode1171 dummy = new ListNode1171(0);
        ListNode1171 current = dummy;
        for (int value : values) {
            current.next = new ListNode1171(value);
            current = current.next;
        }
        return dummy.next;
    }

    // Helper function to print a linked list
    public static void printLinkedList(ListNode1171 head) {
        ListNode1171 current = head;
        while (current != null) {
            System.out.print(current.val);
            if (current.next != null) {
                System.out.print(" -> ");
            }
            current = current.next;
        }
        System.out.println();
    }

    // Test cases
    public static void main(String[] args) {
        REmoveConsecutiveZeroSum1171 sol = new REmoveConsecutiveZeroSum1171();

        // Test case 1
        ListNode1171 head1 = createLinkedList(new int[]{1, 2, -3, 3, 1});
        ListNode1171 result1 = sol.removeZeroSumSublists(head1);
        printLinkedList(result1);  // Expected output: 3 -> 1

        // Test case 2
        ListNode1171 head2 = createLinkedList(new int[]{1, 2, 3, -3, 4});
        ListNode1171 result2 = sol.removeZeroSumSublists(head2);
        printLinkedList(result2);  // Expected output: 1 -> 2 -> 4

        // Test case 3
        ListNode1171 head3 = createLinkedList(new int[]{1, 2, 3, -3, -2});
        ListNode1171 result3 = sol.removeZeroSumSublists(head3);
        printLinkedList(result3);  // Expected output: 1
    }
}
