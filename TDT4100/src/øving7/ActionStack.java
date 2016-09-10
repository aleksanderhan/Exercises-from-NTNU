package øving7;

import java.util.ArrayList;

public class ActionStack {
	
	private ArrayList<Action> actions;
	
	
	public ActionStack() {
		actions = new ArrayList<Action>();
	}
	
	
	public void push(Action act) {
		actions.add(0, act);
	}
	
	
	public Action pop() {
		if (actions.isEmpty()) {
			return null;
		} else {
			return actions.remove(0);
		}
	}
	
	
	public Action peek(int n) {
		if (n < 0 || n > actions.size() - 1) {
			return null;
		} else {
			return actions.get(n);
		}
	}
	
	
	public 	int getSize() {
		return actions.size();
	}	
}
