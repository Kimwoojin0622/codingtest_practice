class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int result = 0;
        for (int i = 0; i < signs.length; i++) {
            if (signs[i]) {
                result += absolutes[i] * 1;
            } else {
                result += absolutes[i] * -1;
            }
        }
        return result;
    }
}