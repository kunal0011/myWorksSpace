package queue;

import java.util.Stack;

class MyQueue<T> {
    private Stack<T> stack1; // Used for dequeue operation
    private Stack<T> stack2; // Used for enqueue operation

    public MyQueue() {
        stack1 = new Stack<>();
        stack2 = new Stack<>();
    }

    public void enqueue(T element) {
        // Move all elements from stack1 to stack2
        while (!stack1.isEmpty()) {
            stack2.push(stack1.pop());
        }
        // Push the new element onto stack1
        stack1.push(element);
        // Move all elements back from stack2 to stack1
        while (!stack2.isEmpty()) {
            stack1.push(stack2.pop());
        }
    }

    public T dequeue() {
        if (isEmpty()) {
            throw new IllegalStateException("Queue is empty");
        }
        // Dequeue operation from stack1
        return stack1.pop();
    }

    public T peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Queue is empty");
        }
        // Peek operation from stack1
        return stack1.peek();
    }

    public boolean isEmpty() {
        return stack1.isEmpty();
    }
}

public class QueueUsingStacks {
    public static void main(String[] args) {
        MyQueue<Integer> queue = new MyQueue<>();
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);

        System.out.println("Dequeue: " + queue.dequeue()); // Dequeue: 1
        System.out.println("Peek: " + queue.peek()); // Peek: 2
        System.out.println("Dequeue: " + queue.dequeue()); // Dequeue: 2
        System.out.println("Is empty: " + queue.isEmpty()); // Is empty: false
        System.out.println("Dequeue: " + queue.dequeue()); // Dequeue: 3
        System.out.println("Is empty: " + queue.isEmpty()); // Is empty: true

        // Trying to dequeue when the queue is empty
        try {
            queue.dequeue();
        } catch (IllegalStateException e) {
            System.out.println("Exception caught: " + e.getMessage()); // Exception caught: Queue is empty
        }
    }
}
