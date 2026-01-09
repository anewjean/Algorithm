class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) {
            return "";
        }

        // 첫 문자열을 prefix로 사용
        String prefix = strs[0];

        // 나머지 문자열들과 비교
        for (int i = 1; i < strs.length; i++) {
            // 현재 문자열이 prefix로 시작하지 않으면 prefix를 한글자씩 줄인다
            while (!strs[i].startsWith(prefix)) {
                prefix = prefix.substring(0, prefix.length() - 1);

                // prefix가 비어 있으면 공통 접두사가 없는 것
                if (prefix.isEmpty()) {
                    return "";
                }
            }
        }

        return prefix;
    }
}
