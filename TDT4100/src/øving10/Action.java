package øving10;

//import java.util.Scanner;

public class Action {
	
	private int[] coordinates;
	
	public Action(int i, int j) {
		coordinates = new int[2];
		coordinates[0] = i;
		coordinates[1] = j;
	}
	
	public int[] getCoordinate() {
		return coordinates;
	}

}
