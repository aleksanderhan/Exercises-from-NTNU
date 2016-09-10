package �ving2;

public class Calculator {
	
	private double firstOperand, secondOperand;
	private char operator;
	
	
	public void setFirstOperand(double operand) {
		this.firstOperand = operand;
	}
	
	
	public void setSecondOperand(double operand) {
		this.secondOperand = operand;
	}
	
	
	public void setOperator(char operator) {
		this.operator = operator;
	}
	
	
	public double calculateResult() throws IllegalArgumentException {
		if (operator == '+') {
			return firstOperand + secondOperand;
		} else if (operator == '-') {
			return firstOperand - secondOperand;
		} else if (operator == '*') {
			return firstOperand * secondOperand;
		} else if (operator == '/') {
			if (secondOperand == 0) {
				throw new IllegalArgumentException("Deling p� 0 er ikke definert.");
			} else {
				return firstOperand / secondOperand;
			}
		} else if (operator =='%') {
			return firstOperand % secondOperand;
		} else {
			throw new IllegalArgumentException("Operatoren m� v�re en av f�lgende: +, -, *, /");
		}
	}
	
	
	public String toString() {
		return "firstOperand: " +  firstOperand + ", secondOperand: " + secondOperand + ", operator: " + operator;
	}
	
	
	public void calculateAndSetFirstOperand() {
		setFirstOperand(calculateResult());
	}
	
	

}
