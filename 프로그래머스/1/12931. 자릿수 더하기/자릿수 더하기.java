import java.util.*;

public class Solution {
    public int solution(int n) {
        int result = 0;
        String tmp = String.valueOf(n);
        for (int i = 0; i < tmp.length(); i++) {
            int t = tmp.charAt(i) - '0';
            result += t;
        }
        return result;
    }
}