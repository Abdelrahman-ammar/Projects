using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using System.Data.SqlClient;
using System.Printing;

namespace hotel_systemm
{
    /// <summary>
    /// Interaction logic for Window1.xaml
    /// </summary>
    public partial class Window1 : Window
    {
        private string gender;
        string path = @"Data Source=DESKTOP-UOPQJ9I;Initial Catalog=Registirations;Integrated Security=True";
        SqlConnection con;
        SqlCommand cmd;
        public Window1()
        {
            InitializeComponent();
            con = new SqlConnection(path);
        }

        private void TextBox_TextChanged(object sender, TextChangedEventArgs e)
        {

        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            if (namebox.Text == "" || nationalbox.Text == "" || mailbox.Text == "" || passwordbox.Password == "" || phonebox.Text == "")
            {
                MessageBox.Show("Please Fill in the Blank");
            }
            else
            {
                try
                {
                    string user_type = "customer";
                    con.Open();
                    cmd = new SqlCommand("insert into registirations (name,nationalID,email,password,phone_number,gender,user_type) values('" + namebox.Text + "','" + nationalbox.Text + "','" + mailbox.Text + "','" + passwordbox.Password + "','" + phonebox.Text + "','" + gender + "','" + user_type + "')", con);
                    cmd.ExecuteNonQuery();
                    con.Close();
                    MessageBox.Show("Signedup, now  please login");
                }
                catch (Exception ex) { MessageBox.Show(ex.Message); }
            }
        }

        private void phonebox_TextChanged(object sender, TextChangedEventArgs e)
        {

        }

        private void genderbtn_Checked(object sender, RoutedEventArgs e)
        {
            gender = (sender as RadioButton).Content.ToString();
        }
    }
}
