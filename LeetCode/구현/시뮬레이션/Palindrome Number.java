class Solution {
    public boolean isPalindrome(int x) {
        // x를 문자로 변환
        String xStr = String.valueOf(x); 
        // 양 끝에서부터 하나씩 좁혀오면서 서로 같은지 비교
        for (int i = 0; i < xStr.length() / 2; i++) {
            if (xStr.charAt(i) != xStr.charAt(xStr.length() - 1 - i)) {
                return false;
            }
        }
        return true;
    }
}
