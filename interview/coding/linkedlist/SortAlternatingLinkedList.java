package linkedlist;

public class SortAlternatingLinkedList {

    // Function to merge two sorted linked lists
    private static ListNode merge(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;

        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                current.next = l1;
                l1 = l1.next;
            } else {
                current.next = l2;
                l2 = l2.next;
            }
            current = current.next;
        }

        if (l1 != null) {
            current.next = l1;
        } else {
            current.next = l2;
        }

        return dummy.next;
    }

    // Function to reverse a linked list
    private static ListNode reverse(ListNode head) {
        ListNode prev = null;
        ListNode current = head;
        while (current != null) {
            ListNode next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        return prev;
    }

    // Function to sort the alternating linked list
    public static ListNode sortAlternatingLinkedList(ListNode head) {
        if (head == null || head.next == null) return head;

        ListNode asc = new ListNode(0); // Dummy head for ascending list
        ListNode desc = new ListNode(0); // Dummy head for descending list
        ListNode ascCurrent = asc;
        ListNode descCurrent = desc;

        ListNode current = head;
        boolean isAscending = true; // Flag to alternate between asc and desc

        while (current != null) {
            if (isAscending) {
                ascCurrent.next = current;
                ascCurrent = ascCurrent.next;
            } else {
                descCurrent.next = current;
                descCurrent = descCurrent.next;
            }
            current = current.next;
            isAscending = !isAscending;
        }

        ascCurrent.next = null;
        descCurrent.next = null;

        // Reverse the descending list to make it ascending
        ListNode reversedDesc = reverse(desc.next);

        // Merge the two ascending lists
        return merge(asc.next, reversedDesc);
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(10);
        head.next = new ListNode(40);
        head.next.next = new ListNode(30);
        head.next.next.next = new ListNode(20);
        head.next.next.next.next = new ListNode(50);
        head.next.next.next.next.next = new ListNode(60);

        ListNode sortedList = sortAlternatingLinkedList(head);

        // Print the sorted list
        ListNode current = sortedList;
        while (current != null) {
            System.out.print(current.val + " ");
            current = current.next;
        }
    }
}
