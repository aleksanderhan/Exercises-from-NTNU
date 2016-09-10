package øving6;

import java.util.ArrayList;

public class CardHand implements CardContainer{
	
	private ArrayList<Card> hand = new ArrayList<Card>();

	
	public int getCardCount() {
		return hand.size();
	}
	
	
	public Card getCard(int n) {
		if (n < 0 || n > getCardCount()) {
			throw new IllegalArgumentException("Kortet er ikke i kortstokken");
		} else {
			return hand.get(n);
		}
	}
	
	
	public void addCard(Card card) {
		hand.add(card);
	}
	
	
	public Card play(int n) {
		return hand.remove(n);
		
	}
	
	
	public String toString() {
		return "CardHand [cardHand=" + hand + "]";
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
}
