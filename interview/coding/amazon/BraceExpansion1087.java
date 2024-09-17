package amazon;

 import java.util.*;

public class BraceExpansion1087 {
    public String[] expand(String s) {
        List<List<Character>> groups = new ArrayList<>();
        int i = 0;

        while (i < s.length()) {
            List<Character> group = new ArrayList<>();
            if (s.charAt(i) == '{') {
                i++;
                while (s.charAt(i) != '}') {
                    if (s.charAt(i) != ',') {
                        group.add(s.charAt(i));
                    }
                    i++;
                }
                i++;
            } else {
                group.add(s.charAt(i));
                i++;
            }
            Collections.sort(group);  // sort to ensure lexicographical order
            groups.add(group);
        }

        List<String> result = new ArrayList<>();
        backtrack(groups, result, new StringBuilder(), 0);
        return result.toArray(new String[0]);
    }

    private void backtrack(List<List<Character>> groups, List<String> result, StringBuilder current, int index) {
        if (index == groups.size()) {
            result.add(current.toString());
            return;
        }

        for (char c : groups.get(index)) {
            current.append(c);
            backtrack(groups, result, current, index + 1);
            current.deleteCharAt(current.length() - 1);
        }
    }
}

