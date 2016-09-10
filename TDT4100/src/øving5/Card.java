package øving5;

public class Card {
	
	private char suit;
	private int face;
	
	
	public Card(char suit, int face) {
		if (face < 1 || face > 13) {
			throw new IllegalArgumentException("Face value must be between 1 and 13");
		} else if ("SHDC".indexOf(suit) == -1) {
			throw new IllegalArgumentException("Suit must be one of the following characters: 'S', 'H', 'D', 'C'");
		} else {
		this.suit = suit;
		this.face = face;
		}
	}
	
	
	public char getSuit() {
		return suit;
	}
	
	
	public int getFace() {
		return face;
	}
	
	
	public String toString() {
		return Character.toString(suit) + face;
	}
	

}
