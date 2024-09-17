package amazon;

/**
 * Definition for singly-linked list.
 */
class ListNode {
    int val;
    ListNode1290 next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode1290 next) { this.val = val; this.next = next; }
}

/**
 * Definition for a binary tree node.
 */
class TreeNode1 {
    int val;
    TreeNode1 left;
    TreeNode1 right;
    TreeNode1() {}
    TreeNode1(int val) { this.val = val; }
    TreeNode1(int val, TreeNode1 left, TreeNode1 right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class LinkedListBt1367 {
    public boolean isSubPath(ListNode1290 head, TreeNode1 root) {
        if (root == null) return false;
        // Check if the current node starts a matching path, or search in the left or right subtree
        return dfs(head, root) || isSubPath(head, root.left) || isSubPath(head, root.right);
    }

    // Helper function to check if there is a matching path from this node
    private boolean dfs(ListNode1290 head, TreeNode1 root) {
        if (head == null) return true;  // If we've matched the entire linked list
        if (root == null) return false;  // If we reach the end of the tree path
        if (root.val != head.val) return false;  // If values don't match

        // Continue to check the next node in the list with the left and right children of the tree
        return dfs(head.next, root.left) || dfs(head.next, root.right);
    }

    // Testing
    public static void main(String[] args) {
        LinkedListBt1367 solution = new LinkedListBt1367();

        // Linked list: 4 -> 2 -> 8
        ListNode1290 head = new ListNode1290(4, new ListNode1290(2, new ListNode1290(8)));

        // Binary tree:
        //       1
        //      / \
        //     4   4
        //    /   / \
        //   2   2   5
        //  /   / \
        // 1   6   8
        TreeNode1 root = new TreeNode1(1);
        root.left = new TreeNode1(4, new TreeNode1(2, new TreeNode1(1),null), null);
        root.right = new TreeNode1(4, new TreeNode1(2, new TreeNode1(6), new TreeNode1(8)), new TreeNode1(5));

        System.out.println("Java Test Result: " + solution.isSubPath(head, root));  // Output: True
    }
}
