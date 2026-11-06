import java.util.Arrays;

class Solution {
    boolean solution(String s) {
        int[] check = {0, 0};
        String s_low = s.toLowerCase();
        
        for (int i = 0; i < s_low.length(); i++) {
            if (s_low.charAt(i) == 'p') {
                check[0] = check[0] + 1;
            } else if (s_low.charAt(i) == 'y') {
                check[1] = check[1] + 1;
            }
        }
        
        return check[0] == check[1];

    }
}