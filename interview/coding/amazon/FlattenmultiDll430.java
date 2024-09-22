package amazon;

import java.util.Stack;

class Node430 {
    public int val;
    public Node430 prev;
    public Node430 next;
    public Node430 child;

    public Node430(int val) {
        this.val = val;
    }
}

public class FlattenmultiDll430 {
    public Node430 flatten(Node430 head) {
        if (head == null) return head;

        Node430 curr = head;
        Stack<Node430> stack = new Stack<>();

        while (curr != null) {
            // If the current node has a child
            if (curr.child != null) {
                // If there is a next node, push it onto the stack
                if (curr.next != null) {
                    stack.push(curr.next);
                }

                // Flatten the child and connect it to the current node
                curr.next = curr.child;
                curr.next.prev = curr;
                curr.child = null;
            }

            // If no next node but there's something in the stack, pop and connect it
            if (curr.next == null && !stack.isEmpty()) {
                curr.next = stack.pop();
                curr.next.prev = curr;
            }

            // Move to the next node
            curr = curr.next;
        }

        return head;
    }

    // Helper function to print the flattened list
    public void printList(Node430 head) {
        Node430 curr = head;
        while (curr != null) {
            System.out.print(curr.val + " -> ");
            curr = curr.next;
        }
        System.out.println("None");
    }

    // Test cases
    public static void main(String[] args) {
        FlattenmultiDll430 sol = new FlattenmultiDll430();

        // Example: Creating a multilevel doubly linked list
        Node430 node1 = new Node430(1);
        Node430 node2 = new Node430(2);
        Node430 node3 = new Node430(3);
        Node430 node4 = new Node430(4);
        Node430 node5 = new Node430(5);
        Node430 node6 = new Node430(6);
        Node430 node7 = new Node430(7);
        Node430 node8 = new Node430(8);
        Node430 node9 = new Node430(9);
        Node430 node10 = new Node430(10);

        node1.next = node2;
        node2.prev = node1;
        node2.next = node3;
        node3.prev = node2;
        node3.child = node7;
        node7.next = node8;
        node8.prev = node7;
        node8.child = node9;
        node9.next = node10;
        node10.prev = node9;
        node3.next = node4;
        node4.prev = node3;
        node4.next = node5;
        node5.prev = node4;
        node5.next = node6;
        node6.prev = node5;

        // Flatten the list
        sol.flatten(node1);

        // Print the flattened list
        sol.printList(node1);  // Expected output: 1 -> 2 -> 3 -> 7 -> 8 -> 9 -> 10 -> 4 -> 5 -> 6 -> None
    }
}

