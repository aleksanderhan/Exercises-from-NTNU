package øving3;

import java.util.Date;


public class Person {

	private String name;
	private String email;
	private char gender;
	private Date birthday;
	
	
	public void setName(String name) {
		if (isValidName(name)) {
			this.name = name;
		}
	}
	
	
	public void setEmail(String email) {	
		if (isValidEmail(email)) {
			this.email = email;
		}
	}
	
	
	public void setBirthday(Date birthday) {
		this.birthday = birthday;
	}
	
	
	public void setGender(char gender) {
		this.gender = gender;
	}
	
	
	public String getName() {
		return name;
	}
	
	
	public String getEmail() {
		return email;
	}
	
	
	public Date getBirthday() {
		return birthday;
	}
	
	
	public char getGender() {
		return gender;
	}
	
	
	private boolean isValidName(String name) {
		return true;
	}
	
	
	private boolean isValidEmail(String email) {
		return true;
	}
	
}
