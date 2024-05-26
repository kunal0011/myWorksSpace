package binarysearch;

public class TransitionPoint {

    public static int findTransitionPoint(int[] arr) {
        int left = 0;
        int right = arr.length - 1;

        // Edge case: if the array has no 1's
        if (arr[right] == 0) {
            return -1;
        }

        while (left < right) {
            int mid = left + (right - left) / 2;

            // If mid element is 1, look in the left half
            if (arr[mid] == 1) {
                right = mid;
            } else {
                // If mid element is 0, look in the right half
                left = mid + 1;
            }
        }

        // left should be the transition point where arr[left] == 1
        return left;
    }

    public static void main(String[] args) {
        int[] arr = {0, 0, 0, 1, 1, 1, 1};
        int transitionPoint = findTransitionPoint(arr);

        if (transitionPoint != -1) {
            System.out.println("The transition point is at index: " + transitionPoint);
        } else {
            System.out.println("There is no transition point in the array.");
        }
    }
}

