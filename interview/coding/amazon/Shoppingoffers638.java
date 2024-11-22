package amazon;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Shoppingoffers638 {
    // Memoization map
    private Map<List<Integer>, Integer> memo = new HashMap<>();

    public int shoppingOffers(List<Integer> price, List<List<Integer>> special, List<Integer> needs) {
        // If the result is already cached, return it
        if (memo.containsKey(needs)) {
            return memo.get(needs);
        }

        // Calculate the cost without any special offer
        int minCost = 0;
        for (int i = 0; i < needs.size(); i++) {
            minCost += needs.get(i) * price.get(i);
        }

        // Try to use each special offer
        for (List<Integer> offer : special) {
            List<Integer> newNeeds = Arrays.asList(new Integer[needs.size()]);
            boolean validOffer = true;

            // Check if we can apply this offer
            for (int i = 0; i < needs.size(); i++) {
                if (offer.get(i) > needs.get(i)) {
                    validOffer = false;
                    break;
                }
                newNeeds.set(i, needs.get(i) - offer.get(i));
            }

            // If the offer is valid, calculate the cost using the offer
            if (validOffer) {
                minCost = Math.min(minCost, shoppingOffers(price, special, newNeeds) + offer.get(offer.size() - 1));
            }
        }

        // Cache and return the result
        memo.put(needs, minCost);
        return minCost;
    }

    // Test cases
    public static void main(String[] args) {
        Shoppingoffers638 sol = new Shoppingoffers638();

        // Test case 1
        List<Integer> price1 = Arrays.asList(2, 5);
        List<List<Integer>> special1 = Arrays.asList(Arrays.asList(3, 0, 5), Arrays.asList(1, 2, 10));
        List<Integer> needs1 = Arrays.asList(3, 2);
        System.out.println(sol.shoppingOffers(price1, special1, needs1));  // Output: 14

        // Test case 2
        List<Integer> price2 = Arrays.asList(2, 3, 4);
        List<List<Integer>> special2 = Arrays.asList(Arrays.asList(1, 1, 0, 4), Arrays.asList(2, 2, 1, 9));
        List<Integer> needs2 = Arrays.asList(1, 2, 1);
        System.out.println(sol.shoppingOffers(price2, special2, needs2));  // Output: 11
    }
}

