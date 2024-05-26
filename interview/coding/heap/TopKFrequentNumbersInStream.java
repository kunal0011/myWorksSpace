package heap;

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Comparator;

public class TopKFrequentNumbersInStream {

    private PriorityQueue<Map.Entry<Integer, Integer>> minHeap;
    private Map<Integer, Integer> frequencyMap;
    private int k;

    public TopKFrequentNumbersInStream(int k) {
        this.k = k;
        this.frequencyMap = new HashMap<>();
        this.minHeap = new PriorityQueue<>(k, Comparator.comparingInt(Map.Entry::getValue));
    }

    public void add(int num) {
        // Update frequency map
        frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);

        // Rebuild the heap
        minHeap.clear();
        for (Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()) {
            minHeap.offer(entry);
            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }
    }

    public int[] getTopK() {
        int[] result = new int[minHeap.size()];
        int i = 0;
        for (Map.Entry<Integer, Integer> entry : minHeap) {
            result[i++] = entry.getKey();
        }
        return result;
    }

    public static void main(String[] args) {
        int k = 4;
        TopKFrequentNumbersInStream topKStream = new TopKFrequentNumbersInStream(k);

        int[] stream = { 5, 2, 1, 3, 2 };

        for (int num : stream) {
            topKStream.add(num);
            System.out.println("Added " + num + ": " + java.util.Arrays.toString(topKStream.getTopK()));
        }

        System.out.println("Final Top " + k + " frequent numbers: " + java.util.Arrays.toString(topKStream.getTopK()));
    }
}
