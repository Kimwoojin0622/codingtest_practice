class Solution {
    public int[] solution(long n) {
        String s = String.valueOf(n);
        int[] result = new int[s.length()];
        
        for (int i = 0; i < s.length(); i++) {
            int tmp = (int)(n % 10);
            result[i] = tmp;
            
            n = n / 10;
        }
        
        return result;
    }
}