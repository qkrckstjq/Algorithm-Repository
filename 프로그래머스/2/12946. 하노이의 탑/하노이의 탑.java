import java.util.*;

class Solution {
    public int[][] solution(int n) {
        List<int[]> result = new ArrayList<>();
        
        
        hanoi(result, n, 1, 2, 3);
        
        return result.toArray(new int[0][]);
    }
    
    public void hanoi(List<int[]> result, int n, int A, int B, int C) {
        if (n == 1) {
            result.add(new int[]{A, C});
        } else {
            hanoi(result, n - 1, A, C, B);
            result.add(new int[]{A, C});
            hanoi(result, n - 1, B, A, C);
        }
    }
}