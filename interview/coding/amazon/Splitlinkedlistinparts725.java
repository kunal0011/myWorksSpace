package amazon;

// Definition for singly-linked list.
class ListNode725 {
    int val;
    ListNode725 next;
    ListNode725() {}
    ListNode725(int val) { this.val = val; }
    ListNode725(int val, ListNode725 next) { this.val = val; this.next = next; }
}

public class Splitlinkedlistinparts725 {
    public ListNode725[] splitListToParts(ListNode725 root, int k) {
        // Count the length of the linked list
        int totalLength = 0;
        ListNode725 current = root;
        while (current != null) {
            totalLength++;
            current = current.next;
        }

        // Determine the size of each part
        int partLength = totalLength / k;  // Minimum size of each part
        int remainder = totalLength % k;   // Extra nodes to distribute

        // Split the linked list
        ListNode725[] result = new ListNode725[k];
        current = root;

        for (int i = 0; i < k; i++) {
            ListNode725 head = current;
            int size = partLength + (i < remainder ? 1 : 0);  // Add one more node to the first 'remainder' parts
            for (int j = 0; j < size - 1 && current != null; j++) {
                current = current.next;
            }
            if (current != null) {
                ListNode725 nextPart = current.next;
                current.next = null;  // Split the current part from the rest
                current = nextPart;
            }
            result[i] = head;
        }

        return result;
    }

    // Helper function to print the linked list
    public static void printLinkedList(ListNode725 node) {
        while (node != null) {
            System.out.print(node.val + " ");
            node = node.next;
        }
        System.out.println();
    }

    // Test the function
    public static void main(String[] args) {
        Splitlinkedlistinparts725 sol = new Splitlinkedlistinparts725();

        // Test case 1
        ListNode725 root1 = new ListNode725(1, new ListNode725(2, new ListNode725(3, new ListNode725(4, new ListNode725(5, new ListNode725(6, new ListNode725(7, new ListNode725(8, new ListNode725(9, new ListNode725(10))))))))));
        int k1 = 3;
        ListNode725[] parts1 = sol.splitListToParts(root1, k1);
        for (ListNode725 part : parts1) {
            sol.printLinkedList(part);  // Output: [1, 2, 3, 4], [5, 6, 7], [8, 9, 10]
        }

        // Test case 2
        ListNode725 root2 = new ListNode725(1, new ListNode725(2));
        int k2 = 5;
        ListNode725[] parts2 = sol.splitListToParts(root2, k2);
        for (ListNode725 part : parts2) {
            sol.printLinkedList(part);  // Output: [1], [2], [], [], []
        }
    }
}
