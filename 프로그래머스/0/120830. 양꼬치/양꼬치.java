class Solution {
    public int solution(int n, int k) {
        int drinks = n / 10;
        drinks = k - drinks;
        int result = (n * 12000) + (drinks * 2000);
        return result;
    }
}