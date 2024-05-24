package tree;



public class TreeIsomorphism {

    // Function to check if two trees are isomorphic
    public static boolean isIsomorphic(TreeNode root1, TreeNode root2) {
        // Base cases
        if (root1 == null && root2 == null) {
            return true; // Both trees are empty
        }
        if (root1 == null || root2 == null) {
            return false; // One tree is empty and the other is not
        }

        // Check if the roots are equal
        if (root1.val != root2.val) {
            return false;
        }

        // Check if either the subtrees' structures match or if their mirror structures match
        return (isIsomorphic(root1.left, root2.left) && isIsomorphic(root1.right, root2.right)) ||
                (isIsomorphic(root1.left, root2.right) && isIsomorphic(root1.right, root2.left));
    }

    public static void main(String[] args) {
        // Example trees
        TreeNode tree1 = new TreeNode(1);
        tree1.left = new TreeNode(2);
        tree1.right = new TreeNode(3);
        tree1.left.left = new TreeNode(4);
        tree1.left.right = new TreeNode(5);

        TreeNode tree2 = new TreeNode(1);
        tree2.left = new TreeNode(3);
        tree2.right = new TreeNode(2);
        tree2.right.left = new TreeNode(5);
        tree2.right.right = new TreeNode(4);

        boolean isIsomorphic = isIsomorphic(tree1, tree2);
        System.out.println("Are the trees isomorphic? " + isIsomorphic); // Output: true
    }
}
