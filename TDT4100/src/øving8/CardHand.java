package øving8;

import java.util.ArrayList;

public class CardHand extends CardContainerImpl {

	
	public CardHand(int maxCardCount) {
		super(maxCardCount);
	}

	public Card play(int n) {
		Card card = getCard(n);
		super.remove(card);
		return card;
	}
	
	public String toString() {
		return "CardHand [cardHand=" + getCardHand() + "]";
	}
	
	public ArrayList<Card> getCardHand() {
		ArrayList<Card> cards = new ArrayList<>();
		for (int n = 0; n < getCardCount() - 1; n++) {
			cards.add(getCard(n));
		}
		return cards;
	}
}
