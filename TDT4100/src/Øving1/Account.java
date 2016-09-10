package øving1;

public class Account {

	public double balance;
	public double interestRate;
	
	public void deposit(double d){
		balance += d;
	}
	
	public void addInterest(){
		balance = balance*(1 + (interestRate/100));	
	}
	
	public String toString(){
		return "Account balance: " + balance + ", Interest rate: " + interestRate;
	}
}
