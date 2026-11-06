import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> li = new ArrayList<>();
        
        li.add(arr[0]);
        
        for (int i = 1; i < arr.length; i++){
            if (arr[i] != arr[i-1]) {
                li.add(arr[i]);
                // System.out.println(li);
            }
        }
        int[] result = new int[li.size()];
        for (int i = 0; i < li.size(); i++){
            result[i] = li.get(i);
        }
        
        return result;
    }
}