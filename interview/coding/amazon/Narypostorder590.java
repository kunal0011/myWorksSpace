package amazon;

import java.util.ArrayList;
import java.util.List;

class Node590 {
    public int val;
    public List<Node590> children;

    public Node590() {}

    public Node590(int _val) {
        val = _val;
    }

    public Node590(int _val, List<Node590> _children) {
        val = _val;
        children = _children;
    }
}

public class Narypostorder590 {
    public List<Integer> postorder(Node590 root) {
        List<Integer> result = new ArrayList<>();
        traverse(root, result);
        return result;
    }

    private void traverse(Node590 node590, List<Integer> result) {
        if (node590 == null) {
            return;
        }
        // Traverse all children first
        for (Node590 child : node590.children) {
            traverse(child, result);
        }
        // Add the current node's value after visiting children
        result.add(node590.val);
    }

    // Test case
    public static void main(String[] args) {
        // Example tree:
        //        1
        //      / | \
        //     3  2  4
        //    / \
        //   5   6
//        Node node5 = new Node(5);
//        Node node6 = new Node(6);
//        Node node3 = new Node(3, List.of(node5, node6));
//        Node node2 = new Node(2);
//        Node node4 = new Node(4);
//        Node root = new Node(1, List.of(node3, node2, node4));

       // Solution sol = new Solution();
      //  System.out.println(sol.postorder(root));  // Expected output: [5, 6, 3, 2, 4, 1]
    }
}


