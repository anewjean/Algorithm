class Solution {
    public int minCostClimbingStairs(int[] cost) {
        /*
        cost[i]는 i번째 계단을 밟을 때 드는 비용
        목표 = n번째 계단 위에 도달하는 것!
        i 번째 계단에 도달하기 위해서는  i-1 또는 i-2번째 계단을 밟는 방법밖에 없으므로
        점화식: dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2]);
        */
        int n = cost.length;
        int prev1 = 0;
        int prev2 = 0;

        for (int i = 2; i <= n; i ++) {
            int curr = Math.min(prev1 + cost[i-1], prev2 + cost[i-2]);
            prev2 = prev1;
            prev1 = curr;
        }

        return prev1;
    }
}
