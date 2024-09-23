package amazon;

import java.util.*;

public class RemoveInValidParenthesis301 {
    public List<String> removeInvalidParentheses(String s) {
        List<String> result = new ArrayList<>();
        Set<String> visited = new HashSet<>();
        Queue<String> queue = new LinkedList<>();

        queue.add(s);
        visited.add(s);
        boolean found = false;

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            for (int i = 0; i < levelSize; i++) {
                String current = queue.poll();
                if (isValid(current)) {
                    result.add(current);
                    found = true;
                }

                if (found) {
                    continue;
                }

                for (int j = 0; j < current.length(); j++) {
                    if (current.charAt(j) != '(' && current.charAt(j) != ')') {
                        continue;
                    }
                    String nextState = current.substring(0, j) + current.substring(j + 1);
                    if (!visited.contains(nextState)) {
                        visited.add(nextState);
                        queue.add(nextState);
                    }
                }
            }

            if (found) {
                break;
            }
        }

        return result;
    }

    private boolean isValid(String s) {
        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') {
                count++;
            } else if (c == ')') {
                count--;
                if (count < 0) {
                    return false;
                }
            }
        }
        return count == 0;
    }
}

