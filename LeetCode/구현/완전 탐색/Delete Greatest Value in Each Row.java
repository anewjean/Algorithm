class Solution {
    public int deleteGreatestValue(int[][] grid) {
        int m = grid.length; // grid의 행 길이
        int n = grid[0].length; // grid의 열 길이
        int totalSum = 0;

        // 각 행마다 max heap 생성
        PriorityQueue<Integer>[] maxHeap = new PriorityQueue[m];
        for (int i = 0; i < m; i++) {
            maxHeap[i] = new PriorityQueue<>(Collections.reverseOrder());
            for (int j = 0; j < n; j++) {
                maxHeap[i].add(grid[i][j]); // max heap에 값 입력 
            }
        }

        // grid가 빌 때까지 아래 로직 반복
        while (n > 0) {
            int finalMaxValue = Integer.MIN_VALUE;

            // 행마다 최대값 삭제 후 최대값 비교
            for (int i = 0; i < m; i++) {
                if (!maxHeap[i].isEmpty()) {
                    int currentMaxValue = maxHeap[i].poll();
                    finalMaxValue = Math.max(finalMaxValue, currentMaxValue);
                }
            }

            // 각 행의 최대값 중 가장 큰 값을 totalSum에 더해줌
            totalSum += finalMaxValue;

            // 열의 수를 1 감소시킴
            n--;
        }

        return totalSum;
    }
}