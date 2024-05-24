package miscellaneous;

public class StockProfit {
    public int maxProfit(int[] prices) {
        if (prices == null || prices.length < 2) {
            return 0;
        }

        int maxProfit = 0;
        int minPrice = prices[0];

        for (int i = 1; i < prices.length; i++) {
            maxProfit = Math.max(maxProfit, prices[i] - minPrice);
            minPrice = Math.min(minPrice, prices[i]);
        }

        return maxProfit;
    }

    public static void main(String[] args) {
        StockProfit stockProfit = new StockProfit();
        int[] prices = {7, 1, 5, 3, 6, 4};
        System.out.println("Maximum profit: " + stockProfit.maxProfit(prices));
    }
}
