package øving8;

import java.util.Iterator;

public class CardContainerIterator implements Iterator<Card> {

	private CardContainer cardContainer;
	private int position;
	private int previous;

	public CardContainerIterator(CardContainer cardContainer) {
		this.cardContainer = cardContainer;
	}

	
	public boolean hasNext() {
		return position < cardContainer.getCardCount();
	}

	
	public Card next() {
		previous = position;
		position++;
		return cardContainer.getCard(previous);
	}

	
	public void remove() {
		throw new UnsupportedOperationException();
	}
}
