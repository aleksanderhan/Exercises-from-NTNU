package øving2;

public class StackProgram {

	public static void main(String[] args) {
		
		Stack stack = new Stack();
		RandomStringGenerator rsg = new RandomStringGenerator();
		
		stack.push(rsg.getRandomString());
		stack.push(rsg.getRandomString());
		System.out.println(stack.getSize());
		System.out.println(stack.peek(0));
		System.out.println(stack.peek(1));
		System.out.println(stack.pop());
		System.out.println(stack.getSize());
		
	}

}
