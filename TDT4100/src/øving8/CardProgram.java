package øving8;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class CardProgram {

	private CardDeck cardDeck, cardDeckTest;
	private CardHand cardHand1, cardHand2;
	
	public void init() {
		cardDeck = new CardDeck(13);
		cardDeckTest = new CardDeck(13);
		cardHand1 = new CardHand(10);
		cardHand2 = new CardHand(10);
	}

	public void run() {
		System.out.println(cardDeck);
		String cardDeckCompareTo = "cardDeckCompareTo = ";
		for (int i=0; i < cardDeck.getCardCount()-1; i++) {
			cardDeckCompareTo += Integer.toString(cardDeck.getCard(i).compareTo(cardDeck.getCard(i+1))) + " ";
		}
		System.out.println(cardDeckCompareTo);
		System.out.println(cardDeck.getCardCount());
		for (int i=0; i<5; i++) {			
			cardDeck.shufflePerfectly();
		}
		System.out.println(cardDeck);
		cardDeckCompareTo = "cardDeckCompareTo = ";
		for (int i=0; i < cardDeck.getCardCount()-1; i++) {
			cardDeckCompareTo += Integer.toString(cardDeck.getCard(i).compareTo(cardDeck.getCard(i+1))) + " ";
		}
		System.out.println( cardDeckCompareTo);
		for (int i=0; i<5; i++) {
			cardDeck.deal(cardHand1, 1);
			cardDeck.deal(cardHand2, 1);
		}
		System.out.println(cardHand1);
		String cardHand1CompareTo = "cardHand1CompareTo = ";
		String cardHand2CompareTo = "cardHand2CompareTo = ";
		for (int i=0; i < cardHand1.getCardCount()-1; i++) {
			cardHand1CompareTo += Integer.toString(cardHand1.getCard(i).compareTo(cardHand1.getCard(i+1))) + " ";
			cardHand2CompareTo += Integer.toString(cardHand2.getCard(i).compareTo(cardHand2.getCard(i+1))) + " ";
		}
		System.out.println(cardHand1CompareTo);
		System.out.println(cardHand2);
		System.out.println(cardHand2CompareTo);
		CardContainerIterator cardIterator = new CardContainerIterator(cardHand1);
		while (cardIterator.hasNext()) {
			System.out.println(cardIterator.next());			
		}
		Card cardTest = new Card('S', 1);
		System.out.println(cardTest.compareTo(cardDeck.getCard(0)));
		
		// test av compareTo()
		System.out.println(cardDeck);
		for (int i=0; i<cardDeck.getCardCount(); i++) {
			Card temp = cardDeck.getCard(i);
			for (int n=i; n<cardDeck.getCardCount();  n++) {
				if (temp.compareTo(cardDeck.getCard(n)) > 0 ) {
					temp = cardDeck.getCard(n);
				}
				cardDeck.remove(temp);
				cardDeck.addCard(i,temp);
			}
		}
		System.out.println("test av compareTo:");
		System.out.println(cardDeck);
		
		// test av CardComparator
			
		CardComparator comp = new CardComparator(true, 'C');
		for (int i=0; i<cardDeck.getCardCount(); i++) {
			Card temp = cardDeck.getCard(i);
			for (int n=i; n<cardDeck.getCardCount();  n++) {
				if (comp.compare(temp, cardDeck.getCard(n)) > 0 ) {
					temp = cardDeck.getCard(n);
				}
				cardDeck.remove(temp);
				cardDeck.addCard(i,temp);
			}
		}
		System.out.println("test av CardComparator:");
		System.out.println(cardDeck);
		
		// Test av Collections.sort
		
		List<Card> cSortTest = cardDeck.getCardDeck();
		Collections.sort(cSortTest, new CardComparator(false, 'C'));
		System.out.println(cardDeck);
		List<Card> cSortTest1 = new ArrayList<Card>();
		for (int i=0; i < cardDeckTest.getCardCount(); i++) {
			cSortTest1.add(cardDeckTest.getCard(i));
		}
		System.out.println(cSortTest1);
		Collections.sort(cSortTest1);
		System.out.println(cSortTest1);
		for (Card c: cardHand1) {
			System.out.println(c);
		}
	}

	public static void main(String[] args) {
		CardProgram program = new CardProgram();
		program.init();
		program.run();
	}

}
