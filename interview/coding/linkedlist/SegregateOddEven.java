package linkedlist;

public class SegregateOddEven {

    public ListNode segregateOddEven(ListNode head) {
        if (head == null) return null;

        ListNode oddHead = null, oddTail = null;
        ListNode evenHead = null, evenTail = null;

        ListNode current = head;

        while (current != null) {
            if (current.val % 2 != 0) { // Odd node
                if (oddHead == null) {
                    oddHead = current;
                    oddTail = oddHead;
                } else {
                    oddTail.next = current;
                    oddTail = oddTail.next;
                }
            } else { // Even node
                if (evenHead == null) {
                    evenHead = current;
                    evenTail = evenHead;
                } else {
                    evenTail.next = current;
                    evenTail = evenTail.next;
                }
            }
            current = current.next;
        }

        // If there are no odd nodes
        if (oddHead == null) {
            return evenHead;
        }

        // If there are no even nodes
        if (evenHead == null) {
            return oddHead;
        }

        // Combine odd and even lists
        oddTail.next = evenHead;
        evenTail.next = null;

        return oddHead;
    }

    // Helper function to print the linked list
    public void printList(ListNode node) {
        while (node != null) {
            System.out.print(node.val + " -> ");
            node = node.next;
        }
        System.out.println("null");
    }

    public static void main(String[] args) {
        SegregateOddEven solution = new SegregateOddEven();

        // Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
        ListNode[] nodeList = new ListNode[8];
        for (int i = 0; i < 8; i++) {
            nodeList[i] = new ListNode(i + 1);
            if (i > 0) {
                nodeList[i - 1].next = nodeList[i];
            }
        }

        ListNode head = nodeList[0];

        // Before segregation
        System.out.println("Original Linked List:");
        solution.printList(head);

        // Segregate odd and even nodes
        ListNode segregatedHead = solution.segregateOddEven(head);

        // After segregation
        System.out.println("Segregated Linked List (Odd followed by Even):");
        solution.printList(segregatedHead);
    }
}
