package øving6;

import java.util.ArrayList;

public class CardDeck implements CardContainer{
	
	private ArrayList<Card> deck = new ArrayList<Card>();
	
	
	public CardDeck(int n) {
		for (int j = 0; j < 4; j++) {
			for (int i = 1; i <= n; i++) {
				if (j == 0) {
					deck.add(new Card('S', i));
				} else if (j == 1) {
					deck.add(new Card('H', i));
				} else if (j == 2) {
					deck.add(new Card('D', i));
				} else {
					deck.add(new Card('C', i));
				}
			}
		}
	}
	
	
	public int getCardCount() {
		return deck.size();
	}
	
	
	public Card getCard(int n) {
		if (n < 0 || n > getCardCount()) {
			throw new IllegalArgumentException("Kortet er ikke i kortstokken");
		} else {
			return deck.get(n);
		}
	}
	
	
	public void deal(CardHand hand, int n) {
		for (int i = n; i > 0; i--) {
			hand.addCard(deck.remove(getCardCount() - 1));
		}
	}
	
	
	public void shufflePerfectly() {
		int n = getCardCount()/2;
		for (int i = 1; i < getCardCount(); i += 2) {
			deck.add(i, deck.remove(n));
			n++;
		}
	}
	
	
	public String toString() {
		return "CardDeck [cardDeck=" + deck + "]";
	}
	
	
	
	
	
	
	
	
	
	
	
	

}
