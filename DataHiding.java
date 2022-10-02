//Data Hidding and Encapsulation in some case

class Encap{

	private int addition;	private int multiplication;

	

	public int getAdd(){

		return addition ;

		

	}

	public int getMul(){

		

		return multiplication ;

	}

	public void setAdd(int n1 , int n2){

		int n3= n1+ n2;

		this. addition = n3;

	}

	

	public void setMul (int m1 ,int m2){

	int m3 = m1 * m2;

	this . multiplication = m3;

	

	}

	//Data Packing 

}

public class Main {

	public static void main(String[] args) {

		Encap zap = new Encap();

		zap.setAdd(12,2);

		zap.setMul(12,2);

		// Data is Hidden and We can't Excess this Data in main method also we Just call our method of Encapsulated which is packed and whatever done in that pack can Execute Accordingly like we can see the values of input num are not accessable in Main Method 

		

		

		//This is the Beauty of Encapsulation 

		

		System.out.println("The multiplication of "+" 12 and "  + "2 is " +zap.getMul());

			System.out.println("The addition of "+ " 12 and " + " 2  is "+ zap.getAdd());

		

} 

}
