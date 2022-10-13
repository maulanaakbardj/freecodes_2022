package DSAS.Sorting;

import java.util.Arrays;

public class twoGreaterELe {
    public static void main(String[] args){
        int[] arr = {5, 17, 100, 11 };
        System.out.println(Arrays.toString(solve(arr)));
    }
    public static int[] solve(int[] A) {
        int[] ans = new int[A.length-2];
        int max1 = -1 , max2 = -1;
        if(A[0] > A[1]) {
            max1 = A[0];
            max2 = A[1];
        }else{
            max1 = A[1];
            max2 = A[0];
        }
        for(int i=2 ; i<A.length ; i++){
            if(A[i] > max1){
                max2 = max1;
                max1 = A[i];
            }else if(A[i] > max2){
                max2 = A[i];
            }
        }
          System.out.println(max1+"  "+max2);
        int ct = 0;
        for(int i = 0 ; i<A.length ; i++){
            if(A[i] < max2){
                ans[ct++] = A[i];
            }
        }
        return ans;
    }
}
