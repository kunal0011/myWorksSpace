package amazon;

public class findsmallergratethantarget744 {
    public char nextGreatestLetter(char[] letters, char target) {
        int left = 0, right = letters.length - 1;

        // If the target is greater than or equal to the last element, wrap around
        if (target >= letters[right]) {
            return letters[0];
        }

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (letters[mid] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return letters[left];
    }

    // Test the function
    public static void main(String[] args) {
        findsmallergratethantarget744 sol = new findsmallergratethantarget744();

        // Test cases
        char[] letters1 = {'c', 'f', 'j'};
        char target1 = 'a';
        System.out.println(sol.nextGreatestLetter(letters1, target1));  // Output: 'c'

        char[] letters2 = {'c', 'f', 'j'};
        char target2 = 'c';
        System.out.println(sol.nextGreatestLetter(letters2, target2));  // Output: 'f'

        char[] letters3 = {'c', 'f', 'j'};
        char target3 = 'd';
        System.out.println(sol.nextGreatestLetter(letters3, target3));  // Output: 'f'

        char[] letters4 = {'a', 'b'};
        char target4 = 'z';
        System.out.println(sol.nextGreatestLetter(letters4, target4));  // Output: 'a'
    }
}

