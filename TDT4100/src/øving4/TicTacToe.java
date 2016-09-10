package øving4;

import java.util.ArrayList;

public class TicTacToe {
	
	private ArrayList<ArrayList<Character>> board;
	private char player;
	private int turns;
	
	public int getTurns() {
		return turns;
	}
	
	
	public TicTacToe() {
		board = new ArrayList<ArrayList<Character>>();
		for (int i = 0; i < 3; i++) {
			board.add(new ArrayList<Character>());
			for (int j = 0; j < 3; j++) {
				board.get(i).add(' ');
			}
		}
		player = 'x';
		this.turns = 0;
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
		if (i < 0 || i > 2 || j < 0  || j > 2) {
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
	
	
	public String coordinates() {
		String line = " -------------------\n";
		return "     Coordinates:\n" + " | 0 0 | 0 1 | 0 2 |\n" + line + 
		" | 1 0 | 1 1 | 1 2 |\n" + line + " | 2 0 | 2 1 | 2 2 |\n";
	}
	
	
	public String toString() {
		String str = "";
		String line = " -------\n";
		for (int i=0; i<3; i++) {
			str += line + " |";
			for (int j=0; j<3; j++) {
				str += board.get(i).get(j).toString();
				if (j < 2) {
					str += "|";
				}
			}
			str += "|\n";		
		}
		str += " -------";
		return str;
	}
	
	
	public boolean hasWon() {
		boolean hasWon = false;
		int diag1 = 0;
		int diag2 = 0;
		for (int i=0; i < 3; i++) {
			int col = 0;
			int row = 0;
			for (int j=0; j < 3; j++) {
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
			if (getPiece(i, 2-i) == player && getPiece(i, 2-i) != ' ') {
				diag2++;
			}
			if (col == 3 || row == 3) {
				hasWon = true;
			}
		}
		if (diag1 == 3 || diag2 == 3) {
			hasWon = true;
		}
		return hasWon;
	}

	
	
	

}



























