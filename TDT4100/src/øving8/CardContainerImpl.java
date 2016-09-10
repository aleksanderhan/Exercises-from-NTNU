package øving8;

import java.util.ArrayList;
import java.util.Iterator;

public class CardContainerImpl implements CardContainer {

	private int maxCardCount;
	private ArrayList<Card> cards;

	public CardContainerImpl(int maxCardCount) {
		this.maxCardCount = maxCardCount;
		cards = new ArrayList<>();
	}

	
	public int getMaxCardCount() {
		return maxCardCount;
	}

	
	public boolean isValidCardCount() {
		return cards.size() < maxCardCount;
	}

	
	public int getCardCount() {
		return cards.size();
	}

	
	public Card getCard(int n) {
		if (n > getCardCount() || n < 0) {
			throw new IllegalArgumentException("Illegal value, too big or too small. cardCount=" + getCardCount());
		} else {
			return cards.get(n);
		}
	}

	
	public void addCard(int index, Card card) {
		if (! isValidCardCount()) {
			throw new IllegalStateException();
		}
		cards.add(index, card);
	}
	
	
	public void addCard(Card card) {
		if (! isValidCardCount()) {
			throw new IllegalStateException();
		}
		cards.add(card);
	}

	
	public void remove(Card card) {
		cards.remove(card);
	}

	
	public Card pop(int n) {
		return cards.remove(n);
	}

	
	public Iterator<Card> iterator() {
		return cards.iterator();
	}
}
