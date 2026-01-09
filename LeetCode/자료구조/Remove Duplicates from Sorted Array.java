class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;

        int i = 0; // 중복 제거된 마지막 위치

        for (int j = 1; j < nums.length; j++) { // 전체 배열 순회 포인터
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }

        return i + 1;
    }
}
