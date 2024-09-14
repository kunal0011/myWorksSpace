package amazon;

public class maximumNoOfAchievableRequest1601 {
    private int maxRequests = 0;

    public int maximumRequests(int n, int[][] requests) {
        int[] netChange = new int[n];
        backtrack(requests, netChange, 0, 0);
        return maxRequests;
    }

    private void backtrack(int[][] requests, int[] netChange, int index, int count) {
        if (index == requests.length) {
            // Check if all buildings have balanced people
            for (int i = 0; i < netChange.length; i++) {
                if (netChange[i] != 0) {
                    return;
                }
            }
            maxRequests = Math.max(maxRequests, count);
            return;
        }

        // Option 1: Include the current request
        netChange[requests[index][0]]--;  // Someone leaves the 'from' building
        netChange[requests[index][1]]++;  // Someone enters the 'to' building
        backtrack(requests, netChange, index + 1, count + 1);

        // Backtrack: Undo the inclusion of the current request
        netChange[requests[index][0]]++;
        netChange[requests[index][1]]--;

        // Option 2: Exclude the current request
        backtrack(requests, netChange, index + 1, count);
    }
}
