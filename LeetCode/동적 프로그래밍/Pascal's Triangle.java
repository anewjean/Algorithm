class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> row = new ArrayList<>();
        
        // rowIndex + 1 길이만큼 초기화
        for (int i = 0; i <= rowIndex; i++) {
            row.add(0);
        }
        row.set(0, 1); // 첫 번째 값은 항상 1

        for (int i = 1; i <= rowIndex; i++) {
            // 오른쪽 → 왼쪽 방향으로 업데이트
            for (int j = i; j > 0; j--) {
                row.set(j, row.get(j) + row.get(j - 1));
            }
        }
        
        return row;
    }
}
