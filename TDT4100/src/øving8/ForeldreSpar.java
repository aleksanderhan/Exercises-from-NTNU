package øving8;

public class ForeldreSpar extends SavingsAccount {

	private int maxYearlyWithdrawals;
	private int remainingWithdrawals;

	public ForeldreSpar(double interestRate, int maxYearlyWithdrawals) {
		super(interestRate);
		this.maxYearlyWithdrawals = maxYearlyWithdrawals;
		remainingWithdrawals = maxYearlyWithdrawals;
	}

	
	@Override
	public void withdraw(double amount) {
		if (remainingWithdrawals <= 0) {
			throw new IllegalStateException("Already used up this years withdrawals");
		}
		super.withdraw(amount);
		remainingWithdrawals--;
	}

	
	@Override
	public void endYearUpdate() {
		super.endYearUpdate();
		remainingWithdrawals = maxYearlyWithdrawals;
	}

	
	public int getRemainingWithdrawals() {
		return remainingWithdrawals;
	}
}
