public class reverseArray {

    public static void main(String[] args) {

        int[] arr={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20};
        System.out.print("Before Reversing : ");
        printArray(arr);
        rArray(arr);
        System.out.print("After Reversing : ");
        printArray(arr);
    }

    private static void rArray(int[] arr) {
        int temp, start=0, end= arr.length-1;
        while(start<end){
            temp=arr[start];
            arr[start]=arr[end];
            arr[end]=temp;
            start++;
            end--;
        }
    }

    private static void printArray(int[] arr) {
        for (int j : arr) {
            System.out.print(j + " ");
        }
        System.out.println();
    }
}
