package linkedlist;

public class LinkedListCycle {

    // Detects cycle in the linked list. Returns true if cycle is found.
    public static boolean detectCycle(ListNode head) {
        if (head == null || head.next == null) {
            return false;
        }

        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {
                return true; // Cycle detected
            }
        }

        return false; // No cycle detected
    }

    // Removes the cycle from the linked list, if present.
    public static void removeCycle(ListNode head) {
        if (head == null || head.next == null) {
            return;
        }

        ListNode slow = head;
        ListNode fast = head;
        boolean cycleDetected = false;

        // Detect cycle
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {
                cycleDetected = true;
                break;
            }
        }

        // If cycle detected, find the start of the cycle
        if (cycleDetected) {
            slow = head;
            // Special case when the start of the cycle is the head of the list
            if (slow == fast) {
                while (fast.next != slow) {
                    fast = fast.next;
                }
                fast.next = null;
                return;
            }
            while (slow.next != fast.next) {
                slow = slow.next;
                fast = fast.next;
            }
            // Remove cycle
            fast.next = null;
        }
    }

    // Utility method to print the linked list
    public static void printList(ListNode head) {
        ListNode temp = head;
        while (temp != null) {
            System.out.print(temp.val + " ");
            temp = temp.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // Creating a linked list with a cycle for testing
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);
        head.next.next.next.next.next = head.next.next; // Creating a cycle

        // Detect and remove cycle
        if (detectCycle(head)) {
            System.out.println("Cycle detected");
            removeCycle(head);
            System.out.println("Cycle removed");
        } else {
            System.out.println("No cycle detected");
        }

        // Print the list after removing the cycle
        printList(head);
    }
}
