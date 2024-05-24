package linkedlist;


public class RearrangeOddEvenLinkedList {
    public static ListNode rearrange(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        // Pointers for even and odd nodes
        ListNode evenDummy = new ListNode(0);
        ListNode evenTail = evenDummy;
        ListNode oddDummy = new ListNode(0);
        ListNode oddTail = oddDummy;

        int position = 1; // Position counter

        // Traverse the linked list
        while (head != null) {
            if (position % 2 == 0) {
                // Even-positioned node
                evenTail.next = head;
                evenTail = evenTail.next;
            } else {
                // Odd-positioned node
                oddTail.next = head;
                oddTail = oddTail.next;
            }
            // Move to the next node
            head = head.next;
            position++;
        }

        // Connect even-positioned nodes with odd-positioned nodes
        evenTail.next = oddDummy.next;
        // Make sure to terminate the end of the odd-positioned nodes
        oddTail.next = null;

        // Return the rearranged list starting from evenDummy's next
        return evenDummy.next;
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
        // Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6
        ListNode head = new ListNode(1);
        ListNode current = head;
        for (int i = 2; i <= 6; i++) {
            current.next = new ListNode(i);
            current = current.next;
        }

        System.out.println("Original linked list:");
        printList(head);

        // Rearrange the linked list
        head = rearrange(head);

        System.out.println("Rearranged linked list:");
        printList(head);
    }
}
