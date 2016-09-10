package �ving3;

/* 
 * 1. Forklar hvorfor metodene over kan sies � v�re en komplett innkapsling av tilstanden?
 * 
 * Det er en komplett innkapsling av tilstanden, siden tilstanden kan bare leses/endres 
 * p� gjennom klassens egne metoder.
 * 
 * 
 * 2. Er denne klassen data-orientert eller tjeneste-orientert? Begrunn svaret!
 * 
 * Klassen er nok mest data-orientert, men er ogs� tjenste-orientert fordi den inneholder
 * metoder som endrer p� tilstanden til objektet.
 */

public class Account {
	
		private double balance;
		private double interestRate;
		
		
		public Account(double balance, double interestRate) {
			if (balance < 0 || interestRate < 0) {
				throw new IllegalArgumentException("balance og interestRate m� begge "
						+ "v�re positive!");
			} else {
				this.balance = balance;
				this.interestRate = interestRate;
			}
		}
		
		
		public double getBalance() {
			return balance;
		}
		
		
		public double getInterestRate() {
			return interestRate;
		}
		
		
		public void setInterestRate(double interestRate) {
			if (interestRate < 0) {
				throw new IllegalArgumentException("interestRate m� v�re st�rre enn 0!");
			} else {
			this.interestRate = interestRate;
			}
		}
		
		
		public void deposit(double amount) {
			if (amount < 0) {
				throw new IllegalArgumentException("amount m� v�re st�rre enn 0!");
			} else {
				this.balance += amount;
			}
		}
		
		
		public void withdraw(double amount) {
			if (amount < 0) {
				throw new IllegalArgumentException("amount m� v�re st�rre enn 0!");
			} else if ((this.balance - amount) < 0) {
				throw new IllegalStateException();
			} else {
				this.balance -= amount;
			}
		}
		
		
		/*
		public static void main(String[] args) {
			Account accountTest = new Account(100.0, 5);
			System.out.println(accountTest.getBalance());
		}
		*/
		 
		
		
		

}

















