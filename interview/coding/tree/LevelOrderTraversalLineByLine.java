package tree;

import java.util.LinkedList;
import java.util.Queue;

public class LevelOrderTraversalLineByLine {
    public static void printLevelOrderLineByLine(TreeNode root) {
        if (root == null) {
            return;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int levelSize = queue.size(); // Number of nodes at the current level

            for (int i = 0; i < levelSize; i++) {
                TreeNode currentNode = queue.poll();
                System.out.print(currentNode.val + " ");

                if (currentNode.left != null) {
                    queue.offer(currentNode.left);
                }

                if (currentNode.right != null) {
                    queue.offer(currentNode.right);
                }
            }

            System.out.println(); // Move to the next line after printing all nodes of the current level
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

        System.out.println("Level order traversal of the binary tree line by line:");
        printLevelOrderLineByLine(root);
    }
}
