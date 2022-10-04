import java.util.Scanner;

public class bubblesort {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a[] = new int[10];

        int i, j, l = a.length, t;

        System.out.println("Enter 10 numbers");
        for (i = 0; i < l; i++) {
            a[i] = sc.nextInt();
        }

        for (i = 0; i < l; i++) {
            for (j = 1; j < (l - i); j++) {
                if (a[j - 1] > a[j]) {
                    t = a[j - 1];
                    a[j - 1] = a[j];
                    a[j] = t;
                }

            }

        }

        System.out.println("Sorted Array");
        for (i = 0; i < l; i++) {
            System.out.println(a[i]);
        }

        sc.close();
    }
}