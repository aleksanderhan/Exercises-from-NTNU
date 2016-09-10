package øving7;

import java.util.ArrayList;

public interface LevelFormat {
	
	TicTacToe readLevel(String path);
	void writeLevel(int N, int M, ArrayList<ArrayList<Character>> board, String path);

}
