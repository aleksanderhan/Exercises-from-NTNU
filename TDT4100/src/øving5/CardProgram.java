package øving5;

public class CardProgram {

	private CardDeck deck;
	private CardHand hand1, hand2;

	
	public void init() {
		deck = new CardDeck(13);
		hand1 = new CardHand();
		hand2 = new CardHand();
	}

	
	public void run() {
		System.out.println(deck);
	
		System.out.println(deck.getCardCount());
		for (int i = 0; i < 1; i++) {			
			deck.shufflePerfectly();
		}
		System.out.println(deck);
		for (int i = 0; i < 5; i++) {
			deck.deal(hand1, 1);
			deck.deal(hand2, 1);
		}
		System.out.println(hand1);
		System.out.println(hand2);
		
	}
	

	public static void main(String[] args) {
		CardProgram program = new CardProgram();
		program.init();
		program.run();
	}

}