class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;

        for (int price : prices) {
            // 지금까지의 최저가 갱신
            if (price < minPrice) {
                minPrice = price;
            }
            // 현재 가격에서 내가 살 수 있는 최저가를 뺀 이익 계산
            else if (price - minPrice > maxProfit) {
                maxProfit = price - minPrice;
            }
        }

        return maxProfit;
    }
}
