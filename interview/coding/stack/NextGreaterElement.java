package stack;

import java.util.Arrays;
import java.util.Stack;

public class NextGreaterElement {

    public static void main(String[] args) {
        int [] arr ={4,3,1,2,1};

        findNextGraterElement(arr);
    }

    private static void findNextGraterElement(int[] arr) {

        int [] nge = new int[arr.length];
        Arrays.fill(nge,-1);

        Stack<Integer> stack  = new Stack<>();
        for(int i=0;i<arr.length;i++) {

            while(!stack.empty() && arr[stack.peek()]< arr[i]) {
                nge[stack.pop()] = arr[i];
            }
            stack.push(i);
        }

        for(int i=0;i<arr.length;i++) {
            System.out.println(nge[i]);
        }
    }
}
