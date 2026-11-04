class Solution {
    public int solution(int[] numbers) {
        int check = 45;
        for (int i = 0; i < numbers.length; i++) {
            check = check - numbers[i];
        }
        return check;
    }
}