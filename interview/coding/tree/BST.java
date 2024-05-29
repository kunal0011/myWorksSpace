package tree;

public class BST {
    TreeNode root;

    // Constructor
    BST() {
        root = null;
    }

    // Insert a val into the BST
    void insert(int val) {
        root = insertRec(root, val);
    }

    TreeNode insertRec(TreeNode root, int val) {
        if (root == null) {
            root = new TreeNode(val);
            return root;
        }

        if (val < root.val) {
            root.left = insertRec(root.left, val);
        } else if (val > root.val) {
            root.right = insertRec(root.right, val);
        }

        return root;
    }

    // Search a val in the BST
    boolean search(int val) {
        return searchRec(root, val);
    }

    boolean searchRec(TreeNode root, int val) {
        if (root == null) {
            return false;
        }

        if (root.val == val) {
            return true;
        }

        if (root.val > val) {
            return searchRec(root.left, val);
        }

        return searchRec(root.right, val);
    }

    // Delete a val from the BST
    void delete(int val) {
        root = deleteRec(root, val);
    }

    TreeNode deleteRec(TreeNode root, int val) {
        if (root == null) {
            return root;
        }

        if (val < root.val) {
            root.left = deleteRec(root.left, val);
        } else if (val > root.val) {
            root.right = deleteRec(root.right, val);
        } else {
            if (root.left == null) {
                return root.right;
            } else if (root.right == null) {
                return root.left;
            }

            root.val = minval(root.right);

            root.right = deleteRec(root.right, root.val);
        }

        return root;
    }

    int minval(TreeNode root) {
        int minval = root.val;
        while (root.left != null) {
            minval = root.left.val;
            root = root.left;
        }
        return minval;
    }

    // In-order traversal to print the BST
    void inorder() {
        inorderRec(root);
    }

    void inorderRec(TreeNode root) {
        if (root != null) {
            inorderRec(root.left);
            System.out.print(root.val + " ");
            inorderRec(root.right);
        }
    }
    public static void main(String[] args) {
        BST tree = new BST();

        // Insert vals into the BST
        tree.insert(50);
        tree.insert(30);
        tree.insert(20);
        tree.insert(40);
        tree.insert(70);
        tree.insert(60);
        tree.insert(80);

        // Print in-order traversal of the BST
        System.out.println("Inorder traversal of the given tree:");
        tree.inorder();

        // Search for a val in the BST
        System.out.println("\nSearch 40 in the BST:");
        System.out.println(tree.search(40) ? "Found" : "Not Found");

        // Delete a val from the BST
        System.out.println("Delete 20");
        tree.delete(20);
        System.out.println("Inorder traversal of the modified tree:");
        tree.inorder();

        System.out.println("\nDelete 30");
        tree.delete(30);
        System.out.println("Inorder traversal of the modified tree:");
        tree.inorder();

        System.out.println("\nDelete 50");
        tree.delete(50);
        System.out.println("Inorder traversal of the modified tree:");
        tree.inorder();
    }
}

