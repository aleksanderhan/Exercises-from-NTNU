package øving8;

public interface CardContainer extends Iterable<Card>{
	
	int getCardCount();
	Card getCard(int n);
	void addCard(int index, Card card);
	void remove(Card card);

}
