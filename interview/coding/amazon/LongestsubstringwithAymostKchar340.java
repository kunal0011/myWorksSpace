package amazon;

import java.util.*;

public class LongestsubstringwithAymostKchar340 {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        if (k == 0) return 0;

        int left = 0, maxLen = 0;
        Map<Character, Integer> charCount = new HashMap<>();

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);

            while (charCount.size() > k) {
                char l = s.charAt(left);
                charCount.put(l, charCount.get(l) - 1);
                if (charCount.get(l) == 0) {
                    charCount.remove(l);
                }
                left++;
            }

            maxLen = Math.max(maxLen, right - left + 1);
        }

        return maxLen;
    }
}
