package linkedlist;


public class DeleteNodeInLinkedList {

    public void deleteNode(ListNode nodeToDelete) {
        // Copy the data from the next node to the current node
        nodeToDelete.val = nodeToDelete.next.val;
        // Delete the next node
        nodeToDelete.next = nodeToDelete.next.next;
    }

    // Utility method to print the linked list
    public void printList(ListNode head) {
        ListNode curr = head;
        while (curr != null) {
            System.out.print(curr.val + " ");
            curr = curr.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        DeleteNodeInLinkedList solution = new DeleteNodeInLinkedList();

        // Create the linked list: 1 -> 2 -> 3 -> 4 -> 5
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);

        // Print the original linked list
        System.out.println("Original linked list:");
        solution.printList(head);

        // Delete the node with value 3
        System.out.println("After deleting node with value 3:");
        solution.deleteNode(head.next.next); // Passing the node with value 3
        solution.printList(head);
    }
}
