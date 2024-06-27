import java.util.*;

class RowInfo {
    int index;
    int soldierCount;

    RowInfo(int index, int soldierCount) {
        this.index = index;
        this.soldierCount = soldierCount;
    }
}

public class Solution {
    public static int[] kWeakestRows(int[][] mat, int k) {
        PriorityQueue<RowInfo> pq = new PriorityQueue<>(new Comparator<RowInfo>() {
            @Override
            public int compare(RowInfo r1, RowInfo r2) {
                if (r1.soldierCount != r2.soldierCount) {
                    return Integer.compare(r1.soldierCount, r2.soldierCount);
                } else {
                    return Integer.compare(r1.index, r2.index);
                }
            }
        });
        
        for (int i = 0; i < mat.length; i++) {
            int soldierCount = countSoldiers(mat[i]);
            pq.add(new RowInfo(i, soldierCount));
        }
        
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = pq.poll().index;
        }
        
        return result;
    }

    private static int countSoldiers(int[] row) {
        int count = 0;
        for (int val : row) {
            if (val == 1) {
                count++;
            } else {
                break;
            }
        }
        return count;
    }
}