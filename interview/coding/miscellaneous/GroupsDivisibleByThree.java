package miscellaneous;

public class GroupsDivisibleByThree {
    static int numOfCombinations(int arr[], int N) {
        // Initialize groups to 0
        int C[] = {0, 0, 0};

        // Increment group with specified remainder
        for (int i = 0; i < N; ++i)
            ++C[arr[i] % 3];

        // Return groups using the formula
        return C[1] * C[2] + C[0] * (C[0] - 1) / 2 + C[0] * (C[0] - 1) * (C[0] - 2) / 6 + C[1] * (C[1] - 1) * (C[1] - 2) / 6 + C[2] * (C[2] - 1) * (C[2] - 2) / 6 + C[0] * C[1] * C[2];
    }

    // Driver code
    public static void main(String[] args) {
        int arr1[] = {1, 5, 7, 2, 9, 14};
        System.out.print(numOfCombinations(arr1, 6) + "\n");
        int arr2[] = {3, 6, 9, 12};
        System.out.print(numOfCombinations(arr2, 4) + "\n");
    }
}
