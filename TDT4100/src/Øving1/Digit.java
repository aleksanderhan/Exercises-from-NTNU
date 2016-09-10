package øving1;

public class Digit {
	
	public int base;
	public int digit;
	
	public Digit(int base) {
		this.base = base;
		this.digit = 0;
	}
	
	
	public int getValue() {
		return digit;
	}
	
	
	public boolean increment() {
		if (digit + 1 < base) {
			digit++;
			return false;
		} else {
			digit = 0;
			return true;
		}
	}
	
	
	public String toString() {
		String value = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
		return Character.toString(value.charAt(digit));
	}
	
	

}












