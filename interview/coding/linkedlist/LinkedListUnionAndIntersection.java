package linkedlist;

import java.util.HashSet;



public class LinkedListUnionAndIntersection {

    // Function to get the union of two linked lists
    public static ListNode getUnion(ListNode head1, ListNode head2) {
        HashSet<Integer> set = new HashSet<>();
        ListNode result = new ListNode(0); // Dummy head for the result list
        ListNode current = result;

        // Add all elements of the first list to the set
        while (head1 != null) {
            if (set.add(head1.val)) { // Add only if it's not already in the set
                current.next = new ListNode(head1.val);
                current = current.next;
            }
            head1 = head1.next;
        }

        // Add all elements of the second list to the set
        while (head2 != null) {
            if (set.add(head2.val)) { // Add only if it's not already in the set
                current.next = new ListNode(head2.val);
                current = current.next;
            }
            head2 = head2.next;
        }

        return result.next; // Return the next of dummy head to get the actual result list
    }

    // Function to get the intersection of two linked lists
    public static ListNode getIntersection(ListNode head1, ListNode head2) {
        HashSet<Integer> set = new HashSet<>();
        ListNode result = new ListNode(0); // Dummy head for the result list
        ListNode current = result;

        // Add all elements of the first list to the set
        while (head1 != null) {
            set.add(head1.val);
            head1 = head1.next;
        }

        // Check elements of the second list against the set
        while (head2 != null) {
            if (set.contains(head2.val)) {
                current.next = new ListNode(head2.val);
                current = current.next;
                set.remove(head2.val); // Remove element to avoid duplicates
            }
            head2 = head2.next;
        }

        return result.next; // Return the next of dummy head to get the actual result list
    }

    // Utility function to print a linked list
    public static void printList(ListNode head) {
        while (head != null) {
            System.out.print(head.val + " ");
            head = head.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // Create first linked list: 1 -> 2 -> 3 -> 4
        ListNode list1 = new ListNode(1);
        list1.next = new ListNode(2);
        list1.next.next = new ListNode(3);
        list1.next.next.next = new ListNode(4);

        // Create second linked list: 3 -> 4 -> 5 -> 6
        ListNode list2 = new ListNode(3);
        list2.next = new ListNode(4);
        list2.next.next = new ListNode(5);
        list2.next.next.next = new ListNode(6);

        // Perform union operation
        ListNode unionList = getUnion(list1, list2);
        System.out.print("Union: ");
        printList(unionList);

        // Perform intersection operation
        ListNode intersectionList = getIntersection(list1, list2);
        System.out.print("Intersection: ");
        printList(intersectionList);
    }
}
