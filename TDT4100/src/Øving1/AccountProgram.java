package øving1;

public class AccountProgram {
	
	private Account account1;
	
	public void init(){
		account1 = new Account();
		account1.interestRate = 0.5;
	}
	
	public void run(){
		System.out.println(account1);
	}
	
	public static void main(String[] args) {
		AccountProgram account = new AccountProgram();
		account.init();
		account.run();
	}

}
