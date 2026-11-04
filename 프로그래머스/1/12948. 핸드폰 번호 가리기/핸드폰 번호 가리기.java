class Solution {
    public String solution(String phone_number) {
        String answer = "";
        int l = phone_number.length() - 4;
        
        for (int i = 0; i < phone_number.length(); i++) {
            if (i < l) {
                answer = answer + '*';
            } else {
                answer = answer + phone_number.charAt(i);
            }
        }
        
        return answer;
    }
}