package linkedlist;


public class SortedLinkestAbsoluteValue {
    public ListNode sortLinkedList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        // Dummy node to simplify edge cases
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        // Pointer to the last node in the sorted portion
        ListNode lastSorted = dummy;

        // Current node to be sorted
        ListNode current = head;

        while (current != null) {
            // If the current value is negative, move it to the front
            if (current.val < 0) {
                lastSorted.next = current.next;  // Remove current from its place
                current.next = dummy.next;       // Move current to the front
                dummy.next = current;            // Update dummy's next to current
                current = lastSorted.next;       // Move to the next node in the original list
            } else {
                // Otherwise, just move the lastSorted pointer
                lastSorted = current;
                current = current.next;
            }
        }

        return dummy.next;
    }

    public static void main(String[] args) {
        SortedLinkestAbsoluteValue sol = new SortedLinkestAbsoluteValue();

        ListNode head = new ListNode(-1);
        head.next = new ListNode(-3);
        head.next.next = new ListNode(2);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(-2);

        ListNode sortedHead = sol.sortLinkedList(head);

        // Print sorted list
        ListNode current = sortedHead;
        while (current != null) {
            System.out.print(current.val + " ");
            current = current.next;
        }
    }
}
