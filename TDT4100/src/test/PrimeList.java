package test;

import java.util.ArrayList;

public class PrimeList {
	
	static boolean isPrime(int n) {
		if (n == 0 || n == 1) {
			return false;
		} else if (n == 2) {
			return true;
		} else {
			for (int i=2; i < n; i++) {
				if (n%i == 0) {
					return false;
				}
			}
			return true;
		}
	}
	 

	public static void main(String[] args) {
		ArrayList<Integer> primeNumbers = new ArrayList<Integer>();
		long start = System.nanoTime();
		for (int i = 0; i < 2000000; i++) {
			if (isPrime(i)) {
				primeNumbers.add(i);
			}
		}
		long end = System.nanoTime();
		System.out.println("Elapsed time = " + (end-start));	
		System.out.println(primeNumbers.size());
		
	}
	
}
