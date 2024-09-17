package amazon;

import java.util.*;

class TreeNode1305 {
    int val;
    TreeNode1305 left;
    TreeNode1305 right;
    TreeNode1305() {}
    TreeNode1305(int val) { this.val = val; }
    TreeNode1305(int val, TreeNode1305 left, TreeNode1305 right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class AllElementInBst1305 {
    public List<Integer> getAllElements(TreeNode1305 root1, TreeNode1305 root2) {
        List<Integer> list1 = new ArrayList<>();
        List<Integer> list2 = new ArrayList<>();

        // Get sorted elements from both trees using inorder traversal
        inorderTraversal(root1, list1);
        inorderTraversal(root2, list2);

        // Merge the two sorted lists
        return mergeSortedLists(list1, list2);
    }

    private void inorderTraversal(TreeNode1305 root, List<Integer> list) {
        if (root == null) {
            return;
        }
        inorderTraversal(root.left, list);
        list.add(root.val);
        inorderTraversal(root.right, list);
    }

    private List<Integer> mergeSortedLists(List<Integer> list1, List<Integer> list2) {
        List<Integer> result = new ArrayList<>();
        int i = 0, j = 0;

        // Merge the two lists
        while (i < list1.size() && j < list2.size()) {
            if (list1.get(i) < list2.get(j)) {
                result.add(list1.get(i));
                i++;
            } else {
                result.add(list2.get(j));
                j++;
            }
        }

        // Append remaining elements
        while (i < list1.size()) {
            result.add(list1.get(i));
            i++;
        }

        while (j < list2.size()) {
            result.add(list2.get(j));
            j++;
        }

        return result;
    }
    TreeNode1305 insertIntoBST(TreeNode1305 root, int val) {
        if (root == null) {
            return new TreeNode1305(val);
        }
        if (val < root.val) {
            root.left = insertIntoBST(root.left, val);
        } else {
            root.right = insertIntoBST(root.right, val);
        }
        return root;
    }

    // Test cases
    public static void main(String[] args) {
        AllElementInBst1305 sol = new AllElementInBst1305();

        // Helper function to insert values into BST

        // Example 1
        TreeNode1305 root1 = null;
        root1 = sol.insertIntoBST(root1, 2);
        root1 = sol.insertIntoBST(root1, 1);
        root1 = sol.insertIntoBST(root1, 4);

        TreeNode1305 root2 = null;
        root2 = sol.insertIntoBST(root2, 1);
        root2 = sol.insertIntoBST(root2, 0);
        root2 = sol.insertIntoBST(root2, 3);

        List<Integer> result = sol.getAllElements(root1, root2);
        System.out.println(result);  // Output should be [0, 1, 1, 2, 3, 4]

        // Example 2: both trees are empty
//        TreeNode1305 root1 = null;
//        TreeNode1305 root2 = null;
//        List<Integer> result = sol.getAllElements(root1, root2);
//        System.out.println(result);  // Output should be []
    }
}
