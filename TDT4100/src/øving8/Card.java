package øving8;

public class Card implements Comparable<Card> {

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
	
	public int compareTo(Card otherCard) {
		String suitRank = "CDHS";
		int suitValue = suitRank.indexOf(Character.toString(getSuit()));
		int otherSuitValue = suitRank.indexOf(Character.toString(otherCard.getSuit()));
		if (suitValue == otherSuitValue) {
			return getFace() - otherCard.getFace();
		} else {
			return suitValue - otherSuitValue;
		}
	}

}
