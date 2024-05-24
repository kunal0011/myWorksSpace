package linkedlist;

public class ReverseKGroup {

    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null || k == 1) return head;

        // Dummy node initialization
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode current = head;
        ListNode prevGroupEnd = dummy;
        ListNode groupStart;
        int count = 0;

        // Count the total number of nodes in the linked list
        while (current != null) {
            count++;
            current = current.next;
        }

        current = head;

        // Loop to reverse every k nodes
        while (count >= k) {
            groupStart = current;
            ListNode prev = null;
            for (int i = 0; i < k; i++) {
                ListNode next = current.next;
                current.next = prev;
                prev = current;
                current = next;
            }
            // Connect the previous group end to the new reversed group start
            prevGroupEnd.next = prev;
            // Connect the end of the reversed group to the start of the next group
            groupStart.next = current;
            // Move prevGroupEnd to the end of the current reversed group
            prevGroupEnd = groupStart;
            // Decrease count by k
            count -= k;
        }

        return dummy.next;
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
        ReverseKGroup solution = new ReverseKGroup();

        // Creating a linked list 1->2->3->4->5->6->7->8
        ListNode[] nodeList = new ListNode[8];
        for (int i = 0; i < 8; i++) {
            nodeList[i] = new ListNode(i + 1);
            if (i > 0) {
                nodeList[i - 1].next = nodeList[i];
            }
        }

        ListNode head = nodeList[0];
        int k = 3;

        // Before reversal
        System.out.println("Original Linked List:");
        solution.printList(head);

        // Reverse in k groups
        ListNode reversedHead = solution.reverseKGroup(head, k);

        // After reversal
        System.out.println("Reversed Linked List in groups of k:");
        solution.printList(reversedHead);
    }

}