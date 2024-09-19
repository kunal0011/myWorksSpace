package amazon;

import java.util.LinkedList;
import java.util.Queue;

// Definition for a binary tree node.
class TreeNode687 {
    int val;
    TreeNode687 left;
    TreeNode687 right;
    TreeNode687() {}
    TreeNode687(int val) { this.val = val; }
    TreeNode687(int val, TreeNode687 left, TreeNode687 right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Lengthoflongestunivaluepath687 {
    private int longest = 0;

    public int longestUnivaluePath(TreeNode687 root) {
        dfs(root);
        return longest;
    }

    private int dfs(TreeNode687 node) {
        if (node == null) {
            return 0;
        }

        // Recursively call dfs for left and right children
        int leftLength = dfs(node.left);
        int rightLength = dfs(node.right);

        // Initialize path lengths through the left and right children
        int leftPath = 0, rightPath = 0;

        // If the left child has the same value, extend the path
        if (node.left != null && node.left.val == node.val) {
            leftPath = leftLength + 1;
        }

        // If the right child has the same value, extend the path
        if (node.right != null && node.right.val == node.val) {
            rightPath = rightLength + 1;
        }

        // Update the longest path found so far
        longest = Math.max(longest, leftPath + rightPath);

        // Return the longest single path going either left or right
        return Math.max(leftPath, rightPath);
    }

    // Helper function to create a binary tree from an array
    public TreeNode687 createTree(Integer[] arr) {
        if (arr.length == 0) {
            return null;
        }
        TreeNode687 root = new TreeNode687(arr[0]);
        Queue<TreeNode687> queue = new LinkedList<>();
        queue.add(root);
        int i = 1;
        while (!queue.isEmpty() && i < arr.length) {
            TreeNode687 current = queue.poll();
            if (arr[i] != null) {
                current.left = new TreeNode687(arr[i]);
                queue.add(current.left);
            }
            i++;
            if (i < arr.length && arr[i] != null) {
                current.right = new TreeNode687(arr[i]);
                queue.add(current.right);
            }
            i++;
        }
        return root;
    }

    // Test the function
    public static void main(String[] args) {
        Lengthoflongestunivaluepath687 sol = new Lengthoflongestunivaluepath687();

        // Test case 1
        Integer[] tree1 = {5, 4, 5, 1, 1, 5};
        TreeNode687 root1 = sol.createTree(tree1);
        System.out.println(sol.longestUnivaluePath(root1));  // Output: 2

        // Test case 2
        Integer[] tree2 = {1, 4, 5, 4, 4, 5};
        TreeNode687 root2 = sol.createTree(tree2);
        System.out.println(sol.longestUnivaluePath(root2));  // Output: 2
    }
}
