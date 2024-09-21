package amazon;

import java.util.*;

class TreeNode655 {
    int val;
    TreeNode655 left;
    TreeNode655 right;
    TreeNode655() {}
    TreeNode655(int val) { this.val = val; }
    TreeNode655(int val, TreeNode655 left, TreeNode655 right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class PrintBt655 {
    public List<List<String>> printTree(TreeNode655 root) {
        int height = getHeight(root);
        int width = (1 << height) - 1;  // Width of the 2D grid is 2^height - 1
        List<List<String>> res = new ArrayList<>();

        // Initialize the grid with empty strings
        for (int i = 0; i < height; i++) {
            List<String> row = new ArrayList<>();
            for (int j = 0; j < width; j++) {
                row.add("");
            }
            res.add(row);
        }

        // Fill the grid recursively
        fill(res, root, 0, (width - 1) / 2, (width - 1) / 2 + 1);
        return res;
    }

    // Helper function to calculate the height of the tree
    private int getHeight(TreeNode655 node) {
        if (node == null) {
            return 0;
        }
        return 1 + Math.max(getHeight(node.left), getHeight(node.right));
    }

    // Recursive function to fill the grid
    private void fill(List<List<String>> res, TreeNode655 node, int r, int c, int levelWidth) {
        if (node == null) {
            return;
        }
        res.get(r).set(c, String.valueOf(node.val));
        if (node.left != null) {
            fill(res, node.left, r + 1, c - levelWidth / 2, levelWidth / 2);
        }
        if (node.right != null) {
            fill(res, node.right, r + 1, c + levelWidth / 2, levelWidth / 2);
        }
    }

    // Test cases
    public static void main(String[] args) {
        PrintBt655 sol = new PrintBt655();

        // Test case 1
        TreeNode655 root1 = new TreeNode655(1,
                new TreeNode655(2, null, new TreeNode655(4)),
                new TreeNode655(3));
        System.out.println(sol.printTree(root1));
        // Output:
        // [["", "", "", "1", "", "", ""],
        //  ["", "2", "", "", "", "3", ""],
        //  ["", "", "4", "", "", "", ""]]

        // Test case 2
        TreeNode655 root2 = new TreeNode655(1, new TreeNode655(2), null);
        System.out.println(sol.printTree(root2));
        // Output:
        // [["", "1", ""],
        //  ["2", "", ""]]
    }
}

