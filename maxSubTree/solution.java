
/**
 * Created by Marcos on 3/31/15.
 */
public class Solution {

    private int maxLen = -1;

    /*class Tree {
        public int x;
        public Tree l;
        public Tree r;
    } */

    public int solution(Tree T) {
        return getMaxPath(T);
    }

    private int getMaxPath(Tree T) {
        if(T == null) {
            return -1;
        }

        int largerPath = Math.max(countLeft(T), countRight(T));
        if(largerPath > maxLen) {
            maxLen = largerPath;
        }

        getMaxPath(T.l);
        getMaxPath(T.r);
        return maxLen;
    }

    private int countLeft(Tree T) {

        Tree traverser = T;
        int count = -1;
        while(traverser != null) {
            traverser = traverser.l;
            count += 1;
        }

        return count;
    }

    private int countRight(Tree T) {

        Tree traverser = T;
        int count = -1;
        while(traverser != null) {
            traverser = traverser.r;
            count += 1;
        }

        return count;
    }
}
