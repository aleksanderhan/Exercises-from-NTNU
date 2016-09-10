using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using Client.Service1;

namespace Client
{
    public partial class Form1 : Form
    {
        private Service1SoapClient soapClient = new Service1SoapClient();

        public Form1()
        {
            InitializeComponent();
        }

        private void searchButton_Click(object sender, EventArgs e)
        {
            listPersonsBox.Items.Clear();
            List<Person> persons = soapClient.search(searchBox.Text).ToList<Person>();
            foreach (Person person in persons)
            {
                listPersonsBox.Items.Add("Age: " + person.Age + ", " + person.FirstName + " " + person.LastName);
            }
        }

        private void listAllButton_Click(object sender, EventArgs e)
        {
            listPersonsBox.Items.Clear();
            List<Person> persons = soapClient.getAllPersons().ToList<Person>();
            foreach (Person person in persons)
            {
                listPersonsBox.Items.Add("Age: " + person.Age + ", " + person.FirstName + " " + person.LastName);
            }
         }

        private void searchBox_TextChanged(object sender, EventArgs e)
        {

        }

        private void listPersonsBox_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

    }
}
