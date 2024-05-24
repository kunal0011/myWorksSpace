package tree;

import java.util.ArrayList;
import java.util.List;


public class CommonNodesInBSTs {

    // Helper method to perform in-order traversal and store elements in a list
    private static void inOrderTraversal(TreeNode root, List<Integer> list) {
        if (root == null) {
            return;
        }
        inOrderTraversal(root.left, list);
        list.add(root.val);
        inOrderTraversal(root.right, list);
    }

    // Method to find common elements in two sorted lists
    private static List<Integer> findCommonElements(List<Integer> list1, List<Integer> list2) {
        List<Integer> common = new ArrayList<>();
        int i = 0, j = 0;

        while (i < list1.size() && j < list2.size()) {
            if (list1.get(i).equals(list2.get(j))) {
                common.add(list1.get(i));
                i++;
                j++;
            } else if (list1.get(i) < list2.get(j)) {
                i++;
            } else {
                j++;
            }
        }
        return common;
    }

    public static void main(String[] args) {
        /* Constructing the first BST:
                   5
                 /   \
                1     10
                     /  \
                    7   15
        */
        TreeNode root1 = new TreeNode(5);
        root1.left = new TreeNode(1);
        root1.right = new TreeNode(10);
        root1.right.left = new TreeNode(7);
        root1.right.right = new TreeNode(15);

        /* Constructing the second BST:
                   10
                 /   \
                7    20
               / \
              5   8
        */
        TreeNode root2 = new TreeNode(10);
        root2.left = new TreeNode(7);
        root2.right = new TreeNode(20);
        root2.left.left = new TreeNode(5);
        root2.left.right = new TreeNode(8);

        // Perform in-order traversal of both BSTs
        List<Integer> list1 = new ArrayList<>();
        List<Integer> list2 = new ArrayList<>();
        inOrderTraversal(root1, list1);
        inOrderTraversal(root2, list2);

        // Find and print common elements
        List<Integer> commonNodes = findCommonElements(list1, list2);
        System.out.println("Common nodes in both BSTs:");
        for (int val : commonNodes) {
            System.out.print(val + " ");
        }
    }
}
