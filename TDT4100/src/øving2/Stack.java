package øving2;

import java.util.ArrayList;

public class Stack {
	
	ArrayList<String> stringList;
	
	
	public Stack() {
		stringList = new ArrayList<String>();
	}
	
	
	public void push(String str) {
		stringList.add(0, str);
	}
	
	
	public String pop() {
		if (stringList.isEmpty()) {
			return null;
		} else {
			return stringList.remove(0);
		}
	}
	
	
	public String peek(int n) {
		if (n < 0 || n > stringList.size() - 1) {
			return null;
		} else {
			return stringList.get(n);
		}
	}
	
	
	public 	int getSize() {
		return stringList.size();
	}
	
	
	public String toString() {
		return "[Stack " + "size: " + getSize() + "]";
	}

}
