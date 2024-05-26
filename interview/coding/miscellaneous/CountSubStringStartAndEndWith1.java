package miscellaneous;

public class CountSubStringStartAndEndWith1 {
    int countSubStr(char str[], int n)
    {
        int m = 0; // Count of 1's in input string

        // Traverse input string and count of 1's in it
        for (int i = 0; i < n; i++) {
            if (str[i] == '1')
                m++;
        }

        // Return count of possible pairs among m 1's
        return m * (m - 1) / 2;
    }

    // Driver program to test the above function
    public static void main(String[] args)
    {
        CountSubStringStartAndEndWith1 count = new CountSubStringStartAndEndWith1();
        String string = "00100101";
        char str[] = string.toCharArray();
        int n = str.length;
        System.out.println(count.countSubStr(str, n));
    }
}
