package linkedlist;

public class SortedInsertCircularLinkedList {
    public ListNode sortedInsert(ListNode head, int x) {
        ListNode newNode = new ListNode(x);

        // If the list is empty, create a single-node circular list
        if (head == null) {
            newNode.next = newNode;
            return newNode;
        }

        ListNode current = head;

        // Special case for inserting before the head (and becoming the new head)
        if (x < head.val) {
            // Find the last node (which points back to the head)
            while (current.next != head) {
                current = current.next;
            }
            // Insert newNode before head and update the last node's next to newNode
            newNode.next = head;
            current.next = newNode;
            return newNode;  // newNode becomes the new head
        }

        // General case: find the position to insert newNode
        while (current.next != head && current.next.val < x) {
            current = current.next;
        }

        // Insert newNode after current and before current.next
        newNode.next = current.next;
        current.next = newNode;

        return head;  // head remains unchanged
    }

    public static void main(String[] args) {
        SortedInsertCircularLinkedList sol = new SortedInsertCircularLinkedList();

        // Creating a circular linked list: 1 -> 2 -> 4 -> 5 -> 1
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(4);
        head.next.next.next = new ListNode(5);
        head.next.next.next.next = head;

        int newValue = 3;
        ListNode newHead = sol.sortedInsert(head, newValue);

        // Print the sorted circular linked list
        ListNode current = newHead;
        do {
            System.out.print(current.val + " ");
            current = current.next;
        } while (current != newHead);
    }
}
