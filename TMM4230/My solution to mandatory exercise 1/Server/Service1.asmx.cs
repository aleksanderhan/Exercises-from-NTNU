using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Services;

namespace Server
{
    /// <summary>
    /// Summary description for Service1
    /// </summary>
    [WebService(Namespace = "http://tempuri.org/")]
    [WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
    [System.ComponentModel.ToolboxItem(false)]
    // To allow this Web Service to be called from script, using ASP.NET AJAX, uncomment the following line. 
    // [System.Web.Script.Services.ScriptService]
    public class Service1 : System.Web.Services.WebService
    {

        PersonList list = new PersonList();

        [WebMethod]
        public List<Person> search(string str)
        {
            return list.search(str);
        }

        [WebMethod]
        public List<Person> searchAge(int age)
        {
            return list.searchAge(age);
        }

        [WebMethod]
        public List<Person> getAllPersons()
        {
            return list.getAllPersons();
        }
    }
}