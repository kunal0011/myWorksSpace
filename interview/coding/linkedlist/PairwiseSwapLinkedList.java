package linkedlist;

public class PairwiseSwapLinkedList {
    public static void pairwiseSwap(ListNode head) {
        ListNode current = head;
        while (current != null && current.next != null) {
            // Swap the values of current and next nodes
            int temp = current.val;
            current.val = current.next.val;
            current.next.val = temp;

            // Move to the next pair of nodes
            current = current.next.next;
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
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);

        System.out.println("Original linked list:");
        printList(head);

        pairwiseSwap(head);

        System.out.println("Linked list after pairwise swapping:");
        printList(head);
    }
}
