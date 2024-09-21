package amazon;

import java.util.HashSet;

class TreeNode653 {
    int val;
    TreeNode653 left;
    TreeNode653 right;
    TreeNode653() {}
    TreeNode653(int val) { this.val = val; }
    TreeNode653(int val, TreeNode653 left, TreeNode653 right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Twosumbst653 {
    public boolean findTarget(TreeNode653 root, int k) {
        HashSet<Integer> set = new HashSet<>();
        return dfs(root, set, k);
    }

    // Helper method for DFS traversal
    private boolean dfs(TreeNode653 node, HashSet<Integer> set, int k) {
        if (node == null) {
            return false;
        }
        // Check if complement exists in the set
        if (set.contains(k - node.val)) {
            return true;
        }
        // Add current node's value to the set
        set.add(node.val);
        // Recursively check left and right subtrees
        return dfs(node.left, set, k) || dfs(node.right, set, k);
    }

    // Test cases
    public static void main(String[] args) {
        Twosumbst653 sol = new Twosumbst653();

        // Test case 1
        TreeNode653 root1 = new TreeNode653(5,
                new TreeNode653(3, new TreeNode653(2), new TreeNode653(4)),
                new TreeNode653(6, null, new TreeNode653(7)));
        System.out.println(sol.findTarget(root1, 9));  // Output: true

        // Test case 2
        TreeNode653 root2 = new TreeNode653(5,
                new TreeNode653(3, new TreeNode653(2), new TreeNode653(4)),
                new TreeNode653(6, null, new TreeNode653(7)));
        System.out.println(sol.findTarget(root2, 28));  // Output: false
    }
}

