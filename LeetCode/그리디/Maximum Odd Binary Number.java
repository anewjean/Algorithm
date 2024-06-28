import java.util.*; 

class Solution {
    public String maximumOddBinaryNumber(String s) {
        // s를 리스트에 넣은 후 마지막 자리에 들어갈 1을 제거한다
        List<String> stringList = new ArrayList<>(Arrays.asList(s.split("")));
        stringList.remove("1");
        
        // 내림차순으로 정렬
        Collections.sort(stringList, Collections.reverseOrder());
		
        // 리스트의 요소들을 하나의 문자열로 병합
        StringBuilder sb = new StringBuilder();
        for (String str: stringList) {
            sb.append(str);
        }
		
        // 마지막에 1을 붙여서 반환
        String result = sb.toString() + "1";
        return result;
    }
}