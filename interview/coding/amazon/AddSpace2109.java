package amazon;
import java.util.*;

public class AddSpace2109 {
    public String addSpaces(String s, int[] spaces) {
        Set<Integer> spaceSet = new HashSet<>();
        for (int index : spaces) {
            spaceSet.add(index);
        }

        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (spaceSet.contains(i)) {
                result.append(' ');
            }
            result.append(s.charAt(i));
        }

        return result.toString();
    }
}
