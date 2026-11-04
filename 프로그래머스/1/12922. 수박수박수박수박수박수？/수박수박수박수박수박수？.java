class Solution {
    public String solution(int n) {
        String[] watermelon = {"수","박"};
        String answer = "";
        
        for (int i = 0; i < n; i++){
            int num = i % 2;
            answer = answer + watermelon[num];
        }
        
        return answer;
    }
}