package tree;


public class SortedArrayToBST {
    // Function to convert sorted array to BST
    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums == null || nums.length == 0) {
            return null;
        }
        return convertToBST(nums, 0, nums.length - 1);
    }

    // Helper function to recursively build the BST
    private TreeNode convertToBST(int[] nums, int left, int right) {
        if (left > right) {
            return null;
        }

        // Find the middle element
        int mid = left + (right - left) / 2;

        // Create the root node with the middle element
        TreeNode root = new TreeNode(mid);

        // Recursively build the left and right subtrees
        root.left = convertToBST(nums, left, mid - 1);
        root.right = convertToBST(nums, mid + 1, right);

        return root;
    }

    // Helper function to print the tree in-order (for testing purposes)
    public void inorderTraversal(TreeNode root) {
        if (root != null) {
            inorderTraversal(root.left);
            System.out.print(root.val + " ");
            inorderTraversal(root.right);
        }
    }

    public static void main(String[] args) {
        SortedArrayToBST solution = new SortedArrayToBST();
        int[] sortedArray = {-10, -3, 0, 5, 9};
        TreeNode bstRoot = solution.sortedArrayToBST(sortedArray);

        System.out.println("In-order traversal of the constructed BST:");
        solution.inorderTraversal(bstRoot);
    }
}
