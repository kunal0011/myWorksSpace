package backtracking;

import java.util.Arrays;

public class AllPermuationOfString {

    public static void main(String[] args) {
        permutate("ABC",0,2);
    }

    private static void permutate(String abc, int i, int i1) {

        if(i==i1) {
            System.out.println(abc);
        }else {
            for (int j = i; j <= i1; j++) {
                abc = swap1(abc, i, j);
                permutate(abc, i + 1, i1);
                abc = swap1(abc, i, j);
            }
        }
    }

    private static String swap1(String abc, int i, int j) {

        char[] charArray = abc.toCharArray();
        char temp = charArray[i];
        charArray[i] = charArray[j];
        charArray[j] = temp;
        return new String(charArray);
    }
}
