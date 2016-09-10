package øving7;

import java.util.Scanner;

public class TicTacToeProgram {

	TicTacToe ttt;
	ActionStack actionStack, undoStack;
	
	public void init() {
		Scanner scanner = new Scanner(System.in);
		System.out.println("Choose board size, and victory conditions separated by whitespace.\n"
				+ "Or write \"load\" to load a previous game: ");
		if (scanner.hasNext("load")) {
			//load
		} else {
			int N = scanner.nextInt();
			int M = scanner.nextInt();
			ttt = new TicTacToe(N, M);
			actionStack = new ActionStack();
			undoStack = new ActionStack();
		}
	}
	
	
	public void run() {	
		int N = ttt.getBoardSize();
		
		while (! ttt.hasWon()) {
			Scanner scanner = new Scanner(System.in);
			
			//Draw condition
			if (ttt.getTurns() >= N*N) {
				break;
			}
			
			System.out.println(ttt);
			System.out.println("It's player " + ttt.getPlayer() + " turn."
					+ " Enter x and y coordinates, separated by whitespace.\n"
					+ "Write undo or redo, to undo or redo the last action respectively.\n"
					+ "Or write \"save\" to save the game: ");
			int i = -1;
			int j = -1;
			boolean undo = false;
			boolean redo = false;
			if (scanner.hasNext("undo")) {
				undo = true;
			} else if (scanner.hasNext("redo")) {
				redo = true;
			} else if (scanner.hasNextInt()) {
				i = scanner.nextInt();
				j = scanner.nextInt();
			} else if (scanner.hasNext("save")) {
				System.out.println("Save as (#filename#.#levelformat#): ");
				scanner.next();
				if (scanner.hasNextLine()) {
					String path = scanner.nextLine();
					System.out.println(path);
					LevelFormat format;
					if (path.endsWith(".lf1")) {
						format = new LevelFormat1();
						format.writeLevel(ttt.getBoardSize(), ttt.getVictoryCondition(), ttt.getBoard(), path);
					} else {
						System.out.println("Format unknown");
						run();
					}
				}
				
			}
			
			if (! ttt.isValidCoordinates(i, j) && undo == false && redo == false) {
				System.out.println("Illegal coordinates. Try again!");
				run();
			} else if (undo == true) {
				Action act = actionStack.pop();
				ttt.undoAction(act);
				undoStack.push(act);
			} else if (redo == true) {
				Action act = undoStack.pop();
				ttt.redoAction(act);
				actionStack.push(act);
			} else {
				if (ttt.setPiece(i, j, ttt.getPlayer())) {	
					Action act = new Action(i, j);
					actionStack.push(act);
					ttt.nextPlayer();
				} else {
					System.out.println("Space is occupied, try again!");
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
		
		
	}


	public static void main(String[] args) {
		TicTacToeProgram program = new TicTacToeProgram();
		program.init();
		program.run();
	}
	
}
