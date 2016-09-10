package øving7;

import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.ArrayList;

public class LevelFormat1 implements LevelFormat {
	
	public TicTacToe readLevel(String path) {
		TicTacToe toe = new TicTacToe(3,3);
		return toe;
		
	}
	
	
	public void writeLevel(int N, int M, ArrayList<ArrayList<Character>> board, String path) {
		try {
			PrintWriter file = new PrintWriter(path);
			file.println("" + N + " " + M + "\n");
			for (ArrayList<Character> row : board) {
				for (Character piece : row) {
					file.println(piece);
				}
				file.println("\n");
			}
			file.close();
			System.out.println("Game Saved.");
		}
		catch (FileNotFoundException e) {
			System.out.println("File not found.");
		}
	}

}
