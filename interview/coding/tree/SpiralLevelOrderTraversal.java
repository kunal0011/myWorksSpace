package tree;

import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;


public class SpiralLevelOrderTraversal {

    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;

        Deque<TreeNode> deque = new LinkedList<>();
        deque.add(root);
        boolean leftToRight = true; // Flag to alternate between left to right and right to left

        while (!deque.isEmpty()) {
            int size = deque.size();
            List<Integer> level = new ArrayList<>();

            for (int i = 0; i < size; i++) {
                if (leftToRight) {
                    TreeNode node = deque.pollFirst();
                    level.add(node.val);
                    if (node.left != null) deque.addLast(node.left);
                    if (node.right != null) deque.addLast(node.right);
                } else {
                    TreeNode node = deque.pollLast();
                    level.add(node.val);
                    if (node.right != null) deque.addFirst(node.right);
                    if (node.left != null) deque.addFirst(node.left);
                }
            }
            result.add(level);
            leftToRight = !leftToRight; // Switch the direction for the next level
        }

        return result;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);

        SpiralLevelOrderTraversal spiralTraversal = new SpiralLevelOrderTraversal();
        List<List<Integer>> result = spiralTraversal.zigzagLevelOrder(root);

        System.out.println("Spiral level order traversal:");
        for (List<Integer> level : result) {
            System.out.println(level);
        }
        // Output:
        // [3]
        // [20, 9]
        // [15, 7]
    }
}
