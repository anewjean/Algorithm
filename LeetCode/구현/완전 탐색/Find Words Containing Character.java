import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

class Solution {
    public List<Integer> findWordsContaining(String[] words, char x) {
        return IntStream.range(0, words.length)
                .filter(i -> words[i].indexOf(x) != -1)
                .boxed()
                .collect(Collectors.toList());
    }
}