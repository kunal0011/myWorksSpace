package linkedlist;



public class SortLinkedList {
    public static void sortList(ListNode head) {
        if (head == null) {
            return;
        }

        // Step 1: Count the number of 0s, 1s, and 2s
        int count0 = 0, count1 = 0, count2 = 0;
        ListNode current = head;

        while (current != null) {
            if (current.val == 0) {
                count0++;
            } else if (current.val == 1) {
                count1++;
            } else {
                count2++;
            }
            current = current.next;
        }

        // Step 2: Update the linked list with the counted values
        current = head;

        while (current != null) {
            if (count0 > 0) {
                current.val = 0;
                count0--;
            } else if (count1 > 0) {
                current.val = 1;
                count1--;
            } else {
                current.val = 2;
                count2--;
            }
            current = current.next;
        }
    }

    public static void printList(ListNode head) {
        ListNode current = head;
        while (current != null) {
            System.out.print(current.val + " ");
            current = current.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // Create a linked list: 0 -> 1 -> 2 -> 1 -> 0 -> 2 -> 1
        ListNode head = new ListNode(0);
        head.next = new ListNode(1);
        head.next.next = new ListNode(2);
        head.next.next.next = new ListNode(1);
        head.next.next.next.next = new ListNode(0);
        head.next.next.next.next.next = new ListNode(2);
        head.next.next.next.next.next.next = new ListNode(1);

        System.out.println("Original list:");
        printList(head);

        sortList(head);

        System.out.println("Sorted list:");
        printList(head);
    }
}
