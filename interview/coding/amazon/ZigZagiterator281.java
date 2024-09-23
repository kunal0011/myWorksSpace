package amazon;

import java.util.*;

public class ZigZagiterator281 {
    private Queue<Iterator<Integer>> queue;

    public ZigZagiterator281(List<Integer> v1, List<Integer> v2) {
        queue = new LinkedList<>();
        if (!v1.isEmpty()) {
            queue.offer(v1.iterator());
        }
        if (!v2.isEmpty()) {
            queue.offer(v2.iterator());
        }
    }

    public int next() {
        Iterator<Integer> currIter = queue.poll();
        int result = currIter.next();
        if (currIter.hasNext()) {
            queue.offer(currIter);
        }
        return result;
    }

    public boolean hasNext() {
        return !queue.isEmpty();
    }
}
