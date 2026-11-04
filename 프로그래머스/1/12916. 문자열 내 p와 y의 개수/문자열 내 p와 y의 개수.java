import java.util.Arrays;

class Solution {
    boolean solution(String s) {
        int[] check = {0, 0};
        s = s.toLowerCase();
        
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'p') {
                check[0]++;
            } else if (s.charAt(i) == 'y') {
                check[1]++;
            }
        }
        
        return check[0] == check[1];

    }
}