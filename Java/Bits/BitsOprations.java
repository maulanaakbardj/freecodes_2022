
package DSAS.Bits;

public class BitsOprations {
    public static void main(String[] args){
        System.out.println(isBit1(14 , 1));
        System.out.println(setBit(10 , 2));
        System.out.println(unSetBit(10 , 1));
        System.out.println(notOperator(10 ));
    }
    static String isBit1(int N , int i){
        // take 1 at ith position and perform AND operation.
        return  ((N) & ( 1<<i))  > 0 ? "Yes" : "No";
    }

    static int setBit(int N , int i){
        return N | (1<<i);
    }
    static int unSetBit(int N , int i){
        return N & (~(1<<i));
    }

    // Ask about this.
    static int notOperator(int N){
        return ~N;
    }
}
