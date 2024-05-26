package string;

import java.util.HashMap;
import java.util.Map;

public class SmallestWindowSubstring {

    public static String minWindow(String s, String t) {
        if (s == null || t == null || s.length() < t.length()) {
            return "";
        }

        // Map to store the frequency of each character in t
        Map<Character, Integer> tFreqMap = new HashMap<>();
        for (char c : t.toCharArray()) {
            tFreqMap.put(c, tFreqMap.getOrDefault(c, 0) + 1);
        }

        int required = tFreqMap.size();
        int left = 0, right = 0;
        int formed = 0;

        // Map to store the frequency of characters in the current window
        Map<Character, Integer> windowCounts = new HashMap<>();

        int[] ans = {-1, 0, 0}; // {window length, left, right}

        while (right < s.length()) {
            char c = s.charAt(right);
            windowCounts.put(c, windowCounts.getOrDefault(c, 0) + 1);

            // Check if the current character added brings us closer to fulfilling the requirement
            if (tFreqMap.containsKey(c) && windowCounts.get(c).intValue() == tFreqMap.get(c).intValue()) {
                formed++;
            }

            // Try to contract the window until it ceases to be 'desirable'
            while (left <= right && formed == required) {
                c = s.charAt(left);

                // Save the smallest window until now
                if (ans[0] == -1 || right - left + 1 < ans[0]) {
                    ans[0] = right - left + 1;
                    ans[1] = left;
                    ans[2] = right;
                }

                // The character at the position pointed by the `left` pointer is no longer a part of the window
                windowCounts.put(c, windowCounts.get(c) - 1);
                if (tFreqMap.containsKey(c) && windowCounts.get(c).intValue() < tFreqMap.get(c).intValue()) {
                    formed--;
                }

                // Move the left pointer ahead, this would help to look for a new window
                left++;
            }

            // Keep expanding the window by moving the right pointer
            right++;
        }

        return ans[0] == -1 ? "" : s.substring(ans[1], ans[2] + 1);
    }

    public static void main(String[] args) {
        String s = "ADOBECODEBANC";
        String t = "ABC";
        String result = minWindow(s, t);
        System.out.println("Smallest window containing all characters: " + result);
    }
}
