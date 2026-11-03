class Solution {
    public double solution(int[] numbers) {
        double result = 0;
        int tmp = 0;
        for (int i = 0; i < numbers.length; i++) {
            tmp = tmp + numbers[i];
        }
        result = (double) tmp / numbers.length;
        return result;
    }
}