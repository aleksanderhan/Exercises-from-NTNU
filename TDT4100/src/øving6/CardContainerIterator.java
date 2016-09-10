package øving6;

public class CardContainerIterator {
	
	private CardContainer CC;
	private int position;
	
	public CardContainerIterator(CardContainer CC) {
		this.CC = CC;
		this.position = 0;
	}
	
	
	public boolean hasNext() {
		return position < CC.getCardCount();
	}
	
	public Card next() {
		position++;
		return CC.getCard(position-1);
	}
	
	public void remove() throws UnsupportedOperationException {
		throw new UnsupportedOperationException("The method is not suporeted.");
	}
	
}
