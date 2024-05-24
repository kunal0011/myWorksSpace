package tree;

import java.util.LinkedList;
import java.util.Queue;


public class LeftViewBinaryTree {

    public static void printLeftView(TreeNode root) {
        if (root == null) {
            return;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            // Number of nodes at the current level
            int levelSize = queue.size();

            // Traverse all nodes of the current level
            for (int i = 0; i < levelSize; i++) {
                TreeNode currentNode = queue.poll();

                // Print the leftmost node at the current level
                if (i == 0) {
                    System.out.print(currentNode.val + " ");
                }

                // Add left node to queue
                if (currentNode.left != null) {
                    queue.offer(currentNode.left);
                }

                // Add right node to queue
                if (currentNode.right != null) {
                    queue.offer(currentNode.right);
                }
            }
        }
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

        System.out.println("Left view of the binary tree:");
        printLeftView(root);
    }
}
