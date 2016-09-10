package øving2;

import java.util.Random;

public class RandomStringGenerator {
	
	Random rand;
	String alphabet = "abcdefghijklmnopqrstuvwxyz";
	
	
	public RandomStringGenerator() {
		rand = new Random();
	}
	
	
	public String getRandomString() {
		String str = "";
		int len = rand.nextInt(100);
		for (int i = 0; i < len; i++) {
			str += alphabet.charAt(rand.nextInt(alphabet.length()));
		}
		return str;
	}

}
