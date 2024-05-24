package tree;


public class NodesAtKDistanceFromRoot {
    public static void printNodesAtKDistance(TreeNode root, int k) {
        if (root == null) {
            return;
        }
        printNodesAtKDistanceUtil(root, k, 0);
    }

    private static void printNodesAtKDistanceUtil(TreeNode node, int k, int distanceFromRoot) {
        if (node == null) {
            return;
        }
        if (distanceFromRoot == k) {
            System.out.print(node.val + " ");
        }
        printNodesAtKDistanceUtil(node.left, k, distanceFromRoot + 1);
        printNodesAtKDistanceUtil(node.right, k, distanceFromRoot + 1);
    }

    public static void main(String[] args) {
        /* Constructed binary tree is:
                   1
                 /   \
                2     3
               / \   / \
              4   5 6   7
                     \
                      8
        */
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(7);
        root.right.left.right = new TreeNode(8);

        int k = 2;
        System.out.println("Nodes at distance " + k + " from root:");
        printNodesAtKDistance(root, k);
    }
}
