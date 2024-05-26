package tree;



public class LongestConsecutiveSequence {

    public int longestConsecutive(TreeNode root) {
        if (root == null) return 0;
        return longestConsecutiveDFS(root, null, 0);
    }

    private int longestConsecutiveDFS(TreeNode node, TreeNode parent, int currentLength) {
        if (node == null) return currentLength;

        // Update the current length based on the value of the current node
        if (parent != null && node.val == parent.val + 1) {
            currentLength++;
        } else {
            currentLength = 1; // Start a new sequence
        }

        // Recursively calculate the lengths of consecutive sequences in the left and right subtrees
        int leftLength = longestConsecutiveDFS(node.left, node, currentLength);
        int rightLength = longestConsecutiveDFS(node.right, node, currentLength);

        // Return the maximum of the lengths from the left and right subtrees
        return Math.max(currentLength, Math.max(leftLength, rightLength));
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.right = new TreeNode(3);
        root.right.left = new TreeNode(2);
        root.right.right = new TreeNode(4);
        root.right.right.right = new TreeNode(5);

        LongestConsecutiveSequence lcs = new LongestConsecutiveSequence();
        System.out.println("Length of longest consecutive sequence: " + lcs.longestConsecutive(root)); // Output: 3
    }
}
