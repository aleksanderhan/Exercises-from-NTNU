package øving8;


import java.util.Comparator;

public class CardComparator implements Comparator<Card> {

	private boolean isAceLargest;
	private String suitRank = "CDHS";
 
	public CardComparator(boolean isAceLargest, char highestSuit) {
		if (suitRank.indexOf(Character.toString(highestSuit)) < 0 && highestSuit != ' ') {
			throw new IllegalArgumentException("Illegal suit value!");
		}
		this.isAceLargest = isAceLargest;
		if (highestSuit == ' ' || highestSuit == 'S') {
		} else {
			if (highestSuit == 'C') {
				suitRank = "DHSC";
			} else if (highestSuit == 'D') {
				suitRank = "CHSD";
			} else if (highestSuit == 'H') {
				suitRank = "CDSH";
			}
		}
	}
	

	

	
	public int compare(Card a, Card b) {
		if (a.getSuit() == b.getSuit()) {
			if (a.getFace() == b.getFace()) {
				return 0;
			} else if (isAceLargest) {
				if (a.getFace() == 1) {
					return 1;
				} else if (b.getFace() == 1) {
					return -1;
				}
			}
			return a.getFace() - b.getFace();
		} else {
			return suitRank.indexOf(Character.toString(a.getSuit())) - suitRank.indexOf(Character.toString(b.getSuit()));
		}
	}

}
