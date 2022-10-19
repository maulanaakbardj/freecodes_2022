  import java.util.*;

public class Main 
{
  
public static void main (String[]args) 
  {
    int n;
System.out.print ("Enter the number to check Palindrome number: ");
    
Scanner s = new Scanner (System.in);
    
n = s.nextInt ();
  
 if(isPalindrome(n))
      System.out.print(n + " is a Palindrome number.");
 else 
     System.out.print(n +" is Not a Palindrome number.");
} 
public static boolean isPalindrome (int n)
  {
    
int r, sum = 0, temp;
    
temp = n;
    
   while (n > 0)
      {
	
         r = n % 10;		//getting remainder  
	     sum = (sum * 10) + r;
         n = n / 10;
      
       }
    
if (temp == sum)
  return true;
 else
  return false;
  
}

}
