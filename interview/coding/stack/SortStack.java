package stack;
import java.util.Stack;

public class SortStack {

    // Function to sort the stack using recursion
    public static void sortStack(Stack<Integer> stack) {
        if (!stack.isEmpty()) {
            // Pop the top element
            int top = stack.pop();

            // Sort the remaining stack
            sortStack(stack);

            // Insert the popped element back in sorted order
            sortedInsert(stack, top);
        }
    }

    // Helper function to insert an element into a sorted stack
    private static void sortedInsert(Stack<Integer> stack, int element) {
        // Base case: Either the stack is empty or the element to be inserted
        // is greater than the top element of the stack
        if (stack.isEmpty() || element > stack.peek()) {
            stack.push(element);
        } else {
            // If the top element is greater, pop it and recurse
            int top = stack.pop();
            sortedInsert(stack, element);

            // Push the top element back after inserting the element
            stack.push(top);
        }
    }

    // Function to print the stack elements
    public static void printStack(Stack<Integer> stack) {
        for (int element : stack) {
            System.out.print(element + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        stack.push(3);
        stack.push(1);
        stack.push(4);
        stack.push(2);
        stack.push(5);

        System.out.println("Original stack:");
        printStack(stack);

        sortStack(stack);

        System.out.println("Sorted stack:");
        printStack(stack);
    }
}
