class Solution {
    public int solution(int slice, int n) {
        int pizza = n % slice;
        if (pizza == 0){
            return n / slice;
        } else {
            return n / slice + 1;
        }
    }
}