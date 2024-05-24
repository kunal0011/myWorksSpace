package tree;

import java.util.*;



class Pair {
    TreeNode node;
    int hd; // Horizontal distance from the root

    Pair(TreeNode node, int hd) {
        this.node = node;
        this.hd = hd;
    }
}

public class TopViewBinaryTree {
    public static void printTopView(TreeNode root) {
        if (root == null) {
            return;
        }

        // Map to store the first node at each horizontal distance
        Map<Integer, TreeNode> topViewMap = new TreeMap<>();
        // Queue for level order traversal
        Queue<Pair> queue = new LinkedList<>();

        // Start with the root node at horizontal distance 0
        queue.offer(new Pair(root, 0));

        while (!queue.isEmpty()) {
            Pair pair = queue.poll();
            TreeNode node = pair.node;
            int hd = pair.hd;

            // If this horizontal distance is not already present in the map, add it
            if (!topViewMap.containsKey(hd)) {
                topViewMap.put(hd, node);
            }

            // Enqueue left child with horizontal distance hd-1
            if (node.left != null) {
                queue.offer(new Pair(node.left, hd - 1));
            }

            // Enqueue right child with horizontal distance hd+1
            if (node.right != null) {
                queue.offer(new Pair(node.right, hd + 1));
            }
        }

        // Print the top view nodes
        for (Map.Entry<Integer, TreeNode> entry : topViewMap.entrySet()) {
            System.out.print(entry.getValue().val + " ");
        }
    }

    public static void main(String[] args) {
        /* Constructed binary tree is:
                  1
                /   \
               2     3
                \   / \
                 4 5   6
                  \
                   7
        */
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.right = new TreeNode(4);
        root.right.left = new TreeNode(5);
        root.right.right = new TreeNode(6);
        root.left.right.right = new TreeNode(7);

        System.out.println("Top view of the binary tree:");
        printTopView(root);
    }
}
