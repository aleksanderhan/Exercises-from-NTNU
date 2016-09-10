package øving4;

import java.util.Scanner;

public class TicTacToeProgram {

	TicTacToe ttt;
	
	public void init() {
		ttt = new TicTacToe();
	}
	
	
	public void run() {
		Scanner scanner = new Scanner(System.in);
		System.out.println(ttt.coordinates());
		while (! ttt.hasWon()) {			
			if (ttt.getTurns() >= 9) {
				break;
			}
			System.out.println(ttt);
			System.out.println("It is player " + ttt.getPlayer() 
					+ " turn. Enter x and y coordinate of next placement (separated by whitespace):");
			int i = scanner.nextInt();
			int j = scanner.nextInt();
			if (! ttt.isValidCoordinates(i, j) ) {
				System.out.println("Illegal coordinates! Try again.");
				run();
			} else {
				if (ttt.setPiece(i, j, ttt.getPlayer())) {
					ttt.nextPlayer();
				} else {
					System.out.println("You cannot set a piece in a occupied space, try again!");
				}
			} 
		}
		System.out.println(ttt);
		if (ttt.hasWon()) {
			ttt.nextPlayer();
			System.out.println("Player " + Character.toString(ttt.getPlayer()) + " has won the game!");
		} else {
			System.out.println("Draw!");
		}
		scanner.close();
	}


	public static void main(String[] args) {
		TicTacToeProgram program = new TicTacToeProgram();
		program.init();
		program.run();
	}
	
}