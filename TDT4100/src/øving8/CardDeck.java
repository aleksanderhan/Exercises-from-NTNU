package øving8;

import java.util.ArrayList;

public class CardDeck extends CardContainerImpl  {
	
	public CardDeck(int n) {
		super(52);	
		if (n < 1 || n > 13) {
			throw new IllegalArgumentException("Illegal value, has to be between 1 and 13");
		} else {
			for (int j = 0; j < 4; j++) {
				for (int i = 1; i <= n; i++) {
					if (j == 0) {
						addCard(new Card('S', i));
					} else if (j==1) {
						addCard(new Card('H', i));
					} else if (j==2) {
						addCard(new Card('D', i));
					} else {
						addCard(new Card('C', i));
					}
				}
			}
		}
	}
	

	public void deal(CardHand deck, int n) {
		for (int i = 0; i < n; i++) {
			deck.addCard(pop((getCardCount() - 1)));
		}
	}

	
	public void shufflePerfectly() {
		int j = getCardCount()/2;
		for (int i = 1; i < getCardCount(); i += 2, j++){
			addCard(i, pop(j));
		}
	}
	

	public String toString() {
		return "CardDeck [cardDeck=" + getCardDeck() + "]";
	}
	
	
	public ArrayList<Card> getCardDeck() {
		ArrayList<Card> cards = new ArrayList<>();
		for (int n=0; n<getCardCount()-1; n++) {
			cards.add(getCard(n));
		}
		return cards;
	}
}
