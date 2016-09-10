using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Server
{
    public class PersonList
    {
        private List<Person> personList = new List<Person>();

        public PersonList()
        {
            personList.Add(new Person("Jens", "Stoltenberg", 55));
            personList.Add(new Person("Erna", "Solberg", 53));
            personList.Add(new Person("Petter", "Solberg", 39));
            personList.Add(new Person("Per", "Person", 34));
            personList.Add(new Person("Olav", "Olvason", 21));
            personList.Add(new Person("Kari", "Traa", 40));
        }

        public List<Person> getAllPersons()
        {
            return personList;
        }

        public List<Person> searchAge(int age)
        {
            List<Person> result = new List<Person>();

            foreach (Person person in personList)
            {
                if (person.Age == age) { result.Add(person); }
            }
            return result;
        }

        public List<Person> search(string str)
        {
            int value = 0;
            bool isValue = Int32.TryParse(str, out value);
            if (isValue)
            {
                return searchAge(value);
            }

            List<Person> result = new List<Person>();

            foreach (Person person in personList)
            {
                if (person.FirstName.ToLower().Contains(str.ToLower()) || 
                    person.LastName.ToLower().Contains(str.ToLower()))
                {
                    result.Add(person);
                }
            }
            return result;
        }

    }
}