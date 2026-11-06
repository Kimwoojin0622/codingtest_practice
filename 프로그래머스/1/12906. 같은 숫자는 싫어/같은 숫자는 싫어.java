import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> li = new ArrayList<>();
        
        li.add(arr[0]);
        
        for (int i = 1; i < arr.length; i++){
            if (arr[i] != arr[i-1]) {
                li.add(arr[i]);
            }
        }
        
        int[] answer = new int[li.size()];
        
        for (int i = 0; i < answer.length; i++){
            answer[i] = li.get(i);
        }


        return answer;
    }
}