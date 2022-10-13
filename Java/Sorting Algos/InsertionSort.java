package DSAS.Sorting;

import java.util.Arrays;

public class InsertionSort {
    public static void main(String[] args){
        int[] arr = {3,46,2,4,675,234,45,1};
       // System.out.println(insertionSort(arr));
      //  System.out.println(bubbleSort(arr));
       // selectionSort(arr);

        Arrays.parallelSort(arr);
        System.out.println(Arrays.toString(arr));
    }
    public static int insertionSort(int[] A) {
        int ct =0;
        for(int i =1 ; i<A.length ; i++){
            for(int j = i ; j>=1 ; j--){
                while(A[j] < A[j-1]){
                    ct++;
                    swap(A , j-1 , j);
                    System.out.println(Arrays.toString(A));
                }
            }
        }
        System.out.println(Arrays.toString(A));
        return ct;
    }
    static int bubbleSort(int[] A){
        int ct =0;
        int n= A.length;
        for(int  i=0 ; i<n ; i++){
            for(int j =0 ; j<n-i-1; j++){
                if(A[j] > A[j+1]){
                    swap(A , j, j+1);
                    ct++;
                }
            }
        }
        System.out.println(Arrays.toString(A));
        return ct;
    }

    static void selectionSort(int[] A){
        int n = A.length;
        for(int i =0 ; i<n-1 ; i++){
            int minVal = A[i];
            int minidx = i;
            for(int j = i+1 ; j<n; j++){
                if(minVal > A[j]){
                    minVal = A[j];
                    minidx = j;
                }
            }
            swap(A , i , minidx);
        }
        System.out.println(Arrays.toString(A));
    }

    static void swap(int[] A , int i , int j){
        int t = A[i];
        A[i] = A[j];
        A[j] = t;
    }
}
