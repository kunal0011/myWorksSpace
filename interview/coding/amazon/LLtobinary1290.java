package amazon;

// Definition for singly-linked list.
class ListNode1290 {
    int val;
    ListNode1290 next;
    ListNode1290() {}
    ListNode1290(int val) { this.val = val; }
    ListNode1290(int val, ListNode1290 next) { this.val = val; this.next = next; }
}

public class LLtobinary1290 {
    public int getDecimalValue(ListNode1290 head) {
        int num = 0;
        while (head != null) {
            // Left shift num by 1 bit (equivalent to multiplying by 2)
            // and add the current node's value
            num = num * 2 + head.val;
            head = head.next;
        }
        return num;
    }

    // Helper function to create a linked list from an array
    public static ListNode1290 createLinkedList(int[] values) {
        ListNode1290 dummy = new ListNode1290();
        ListNode1290 current = dummy;
        for (int value : values) {
            current.next = new ListNode1290(value);
            current = current.next;
        }
        return dummy.next;
    }

    // Test cases
    public static void main(String[] args) {
        LLtobinary1290 sol = new LLtobinary1290();

        // Test case 1
        ListNode1290 head1 = createLinkedList(new int[]{1, 0, 1});
        int result1 = sol.getDecimalValue(head1);
        assert result1 == 5 : "Test case 1 failed: " + result1;

        // Test case 2
        ListNode1290 head2 = createLinkedList(new int[]{0});
        int result2 = sol.getDecimalValue(head2);
        assert result2 == 0 : "Test case 2 failed: " + result2;

        // Test case 3
        ListNode1290 head3 = createLinkedList(new int[]{1});
        int result3 = sol.getDecimalValue(head3);
        assert result3 == 1 : "Test case 3 failed: " + result3;

        System.out.println("All test cases passed!");
    }
}
