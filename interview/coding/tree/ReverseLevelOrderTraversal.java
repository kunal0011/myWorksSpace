package tree;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;



public class ReverseLevelOrderTraversal {
    public void reverseLevelOrderTraversal(TreeNode root) {
        if (root == null) return;

        Queue<TreeNode> queue = new LinkedList<>();
        Stack<TreeNode> stack = new Stack<>();

        queue.add(root);

        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            stack.push(node);

            if (node.right != null) {
                queue.add(node.right);
            }
            if (node.left != null) {
                queue.add(node.left);
            }
        }

        while (!stack.isEmpty()) {
            System.out.print(stack.pop().val + " ");
        }
    }

    public static void main(String[] args) {
        /* Constructing a sample binary tree
                1
               / \
              2   3
             / \ / \
            4  5 6  7
        */
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(7);

        ReverseLevelOrderTraversal traversal = new ReverseLevelOrderTraversal();
        System.out.print("Reverse Level Order Traversal: ");
        traversal.reverseLevelOrderTraversal(root);
    }
}
