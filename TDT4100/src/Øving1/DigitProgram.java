package øving1;

public class DigitProgram {
	
	Digit digit;
	
	public void init() {
		digit = new Digit(16);
	}
	
	public void run() {
		System.out.println(digit);
		for (int i = 0; i < 10; i++) {
			digit.increment();
		}
		System.out.println(digit);
	}

	public static void main(String[] args) {
		DigitProgram digitProgram = new DigitProgram();
		digitProgram.init();
		digitProgram.run();
	}

}
