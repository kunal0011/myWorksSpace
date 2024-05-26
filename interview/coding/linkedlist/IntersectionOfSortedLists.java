package linkedlist;
public class IntersectionOfSortedLists {

    public static ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode dummy = new ListNode(0); // Dummy node to form the new list
        ListNode tail = dummy;

        ListNode p1 = headA;
        ListNode p2 = headB;

        // Traverse both lists
        while (p1 != null && p2 != null) {
            if (p1.val == p2.val) {
                tail.next = new ListNode(p1.val);
                tail = tail.next;
                p1 = p1.next;
                p2 = p2.next;
            } else if (p1.val < p2.val) {
                p1 = p1.next;
            } else {
                p2 = p2.next;
            }
        }

        return dummy.next;
    }

    public static void main(String[] args) {
        // Create first sorted linked list: 1 -> 2 -> 4 -> 6
        ListNode headA = new ListNode(1);
        headA.next = new ListNode(2);
        headA.next.next = new ListNode(4);
        headA.next.next.next = new ListNode(6);

        // Create second sorted linked list: 2 -> 4 -> 6 -> 8
        ListNode headB = new ListNode(2);
        headB.next = new ListNode(4);
        headB.next.next = new ListNode(6);
        headB.next.next.next = new ListNode(8);

        // Find intersection
        ListNode intersection = getIntersectionNode(headA, headB);

        // Print intersection
        ListNode current = intersection;
        while (current != null) {
            System.out.print(current.val + " ");
            current = current.next;
        }
        // Output: 2 4 6
    }
}
