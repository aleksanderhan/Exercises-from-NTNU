package øving8;

public class SavingsAccount implements Account {

	private double balance;
	private double interestRate;

	public SavingsAccount(double interestRate) throws IllegalArgumentException{
		if (interestRate < 0) {
			throw new IllegalArgumentException("interestRate kan ikke være negativ! interestRate som ble gitt var: " + interestRate);
		} else {
			balance = 0;
			this.interestRate = interestRate;
		}
	}

	
	public double getBalance() {
		return balance;
	}
	
	
	protected boolean isValidAmount(double amount) {
		return amount > 0;
	}
	
	
	public void deposit(double amount) throws IllegalArgumentException {
		if(! isValidAmount(amount)){
			throw new IllegalArgumentException("Illegal amount");
		} 
		balance += amount;
	}
	
	
	protected boolean isValidWithdrawAmount(double amount) {
		return amount < balance;
	}
	
	
	public void withdraw(double amount) {
		if (! isValidAmount(amount)) {
			throw new IllegalArgumentException("Kan ikke ta ut negativt beløp! Beløpet var: " + amount);
		} else if (! isValidWithdrawAmount(amount)) {
			throw new IllegalStateException("Kan ikke ta ut beløp som er større enn balance! " + amount + " forsøkt tatt ut,"
					+ " balance = " + balance);
		} else {
			balance -= amount;
		}
	}

	
	public void endYearUpdate() {
		balance += interestRate*balance;
	}

	
	public String toString() {
		return "Account balance= " + balance + " interestRate= " + interestRate;
	}
}
