package linkedlist;


public class NthNodeFromEnd {
    public static ListNode findNthFromEnd(ListNode head, int n) {
        if (head == null || n <= 0) {
            return null;
        }

        ListNode p = head;
        ListNode q = head;

        // Move p forward by n nodes
        for (int i = 0; i < n; i++) {
            if (p == null) {
                // If n is greater than the number of nodes in the list
                return null;
            }
            p = p.next;
        }

        // Move both pointers until p reaches the end of the list
        while (p != null) {
            p = p.next;
            q = q.next;
        }

        // q is now at the nth node from the end
        return q;
    }

    public static void main(String[] args) {
        // Example linked list: 1 -> 2 -> 3 -> 4 -> 5
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);

        int n = 2;
        ListNode nthNode = findNthFromEnd(head, n);
        if (nthNode != null) {
            System.out.println("The " + n + "-th node from the end is: " + nthNode.val);
        } else {
            System.out.println("Invalid input or node does not exist.");
        }
    }
}

