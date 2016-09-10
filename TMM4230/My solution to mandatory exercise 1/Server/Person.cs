using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Server
{
    public class Person
    {
        private String firstName;
        private String lastName;
        private int age;

        public Person()
        { 
        
        }

        public Person(String firstName, String lastName, int age)
        {
            this.firstName = firstName;
            this.lastName = lastName;
            this.age = age;
        }

        public int Age
        {
            get { return age; }
            set { age = value; }
        }

        public String LastName
        {
            get { return lastName; }
            set { lastName = value; }
        }

        public String FirstName
        {
            get { return firstName; }
            set { lastName = value; }
        }


    }
}