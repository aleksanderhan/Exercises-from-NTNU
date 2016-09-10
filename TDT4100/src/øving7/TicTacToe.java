package øving7;

import java.util.ArrayList;

public class TicTacToe {
	
	private ArrayList<ArrayList<Character>> board;
	private char player;
	private int turns;
	private int N, M;
	
	public int getTurns() {
		return turns;
	}
	
	
	public int getBoardSize() {
		return N;
	}
	
	
	public int getVictoryCondition() {
		return M;
	}
	
	
	public ArrayList<ArrayList<Character>> getBoard() {
		return board;
	}
	
	
	public TicTacToe(int N, int M) throws IllegalArgumentException {
		board = new ArrayList<ArrayList<Character>>();
		for (int i = 0; i < N; i++) {
			board.add(new ArrayList<Character>());
			for (int j = 0; j < N; j++) {
				board.get(i).add(' ');
			}
		}
		player = 'x';
		this.turns = 0;
		if (N >= M && N >= 3 && M >= 3) {
			this.N = N;
			this.M = M;
		} else {
			throw new IllegalArgumentException();
		}
	}
	
	
	public boolean setPiece(int i, int j, Character piece) {
		if (board.get(i).get(j) == ' ') {
			board.get(i).set(j, piece);
			return true;
		} else {
			return false;
		}
	}
	
	
	public Character getPiece(int i, int j) {
		return board.get(i).get(j);
	}
	
	
	public boolean isValidCoordinates(int i, int j) {
		if (i < 0 || i > N-1 || j < 0  || j > N-1) {
			return false;
		} else {
			return true;
		}
	}
	
	
	public char getPlayer() {
		return player;
	}
	
	
	public void nextPlayer() {
		if (player == 'x') {
			this.player = 'o';
		} else {
			this.player = 'x';
		}
		this.turns++;
	}
	
	
	public String toString() {
		String str = "";
		String line = " ";
		for (int i=0; i<N; i++) {
			line += "--";
		}
		line += "-\n ";
		for (int i=0; i<N; i++) {
			str += line + "|";
			for (int j=0; j<N; j++) {
				str += board.get(i).get(j).toString();
				if (j < N-1) {
					str += "|";
				}
			}
			str += "|\n";		
		}
		str += line;
		return str;
	}
	
	
	public boolean hasWon() {
		boolean hasWon = false;
		int diag1 = 0;
		int diag2 = 0;
		for (int i=0; i < N; i++) {
			int col = 0;
			int row = 0;
			for (int j=0; j < N; j++) {
				if (getPiece(i, j) != player && getPiece(i, j) != ' ') {
					col++;
				} 
				if (getPiece(j, i) != player && getPiece(j, i) != ' ') {
					row++;
				}
			}
			if (getPiece(i, i) != player && getPiece(i, i) != ' ') {
				diag1++;
			}
			if (getPiece(i, N-1-i) == player && getPiece(i, N-1-i) != ' ') {
				diag2++;
			}
			if (col == M || row == M) {
				hasWon = true;
			}
		}
		if (diag1 == M || diag2 == M) {
			hasWon = true;
		}
		return hasWon;
	}
	
	
	public void undoAction(Action act) {
		board.get(act.getCoordinate()[0]).set(act.getCoordinate()[1], ' ');
		nextPlayer();
	}
	
	
	public void redoAction(Action act) {
		board.get(act.getCoordinate()[0]).set(act.getCoordinate()[1], getPlayer());
		nextPlayer();
		
	}

	
	
	

}



























