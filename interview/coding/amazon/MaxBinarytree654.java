package amazon;

import java.util.*;
// Definition for a binary tree node.
class TreeNode654 {
    int val;
    TreeNode654 left;
    TreeNode654 right;
    TreeNode654() {}
    TreeNode654(int val) { this.val = val; }
    TreeNode654(int val, TreeNode654 left, TreeNode654 right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class MaxBinarytree654 {
    public TreeNode654 constructMaximumBinaryTree(int[] nums) {
        return build(nums, 0, nums.length);
    }

    // Helper method to build the tree recursively
    private TreeNode654 build(int[] nums, int left, int right) {
        if (left == right) {
            return null; // Base case: no elements
        }

        // Find the index of the maximum element in the range [left, right)
        int maxIndex = maxIndex(nums, left, right);

        // Create the root node with the maximum value
        TreeNode654 root = new TreeNode654(nums[maxIndex]);

        // Recursively build the left subtree
        root.left = build(nums, left, maxIndex);

        // Recursively build the right subtree
        root.right = build(nums, maxIndex + 1, right);

        return root;
    }

    // Helper method to find the index of the maximum element
    private int maxIndex(int[] nums, int left, int right) {
        int maxIndex = left;
        for (int i = left + 1; i < right; i++) {
            if (nums[i] > nums[maxIndex]) {
                maxIndex = i;
            }
        }
        return maxIndex;
    }

    // Test cases
    public static void main(String[] args) {
        MaxBinarytree654 sol = new MaxBinarytree654();

        // Test case 1
        int[] nums1 = {3, 2, 1, 6, 0, 5};
        TreeNode654 root1 = sol.constructMaximumBinaryTree(nums1);
        System.out.println(preorderTraversal(root1));  // Output: [6, 3, 2, 1, 5, 0]

        // Test case 2
        int[] nums2 = {1, 2, 3, 4, 5};
        TreeNode654 root2 = sol.constructMaximumBinaryTree(nums2);
        System.out.println(preorderTraversal(root2));  // Output: [5, 4, 3, 2, 1]
    }

    // Helper function to print the tree in preorder for testing
    public static List<Integer> preorderTraversal(TreeNode654 root) {
        List<Integer> result = new ArrayList<>();
        preorder(root, result);
        return result;
    }

    // Recursive preorder traversal
    private static void preorder(TreeNode654 node, List<Integer> result) {
        if (node == null) {
            return;
        }
        result.add(node.val);
        preorder(node.left, result);
        preorder(node.right, result);
    }
}
