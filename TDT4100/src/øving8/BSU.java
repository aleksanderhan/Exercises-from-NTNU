package øving8;

public class BSU extends SavingsAccount {
	
	private double yearlyMaxDeposit;
	private double thisYearsDeposits;
	
	public BSU(double interestrate, double yearlyMaxDeposit) {
		super(interestrate);
		this.yearlyMaxDeposit = yearlyMaxDeposit;
	}
	
	
	@Override
	protected boolean isValidAmount(double amount) {
		if ((amount + thisYearsDeposits) > yearlyMaxDeposit) {
			throw new IllegalStateException("Illegal amount");
		}
		return super.isValidAmount(amount);
	}
	
	
	@Override
	protected boolean isValidWithdrawAmount(double amount) {
		return amount <= thisYearsDeposits;
	}
	
	
	@Override
	public void deposit(double amount) throws IllegalArgumentException {
		super.deposit(amount);
		thisYearsDeposits += amount;
	}
	
	
	@Override
	public void endYearUpdate() {
		super.endYearUpdate();
		thisYearsDeposits = 0;
	}
	
	
	@Override
	public void withdraw(double amount) {
		super.withdraw(amount);
		thisYearsDeposits -= amount;
	}
	
	
	public double getTaxDeduction() {
		return thisYearsDeposits*0.2;
	}
}
