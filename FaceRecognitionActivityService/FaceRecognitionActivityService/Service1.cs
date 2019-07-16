using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Diagnostics;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Runtime.CompilerServices;
using System.ServiceProcess;
using System.Text;
using System.Threading.Tasks;
using System.Timers;

namespace FaceRecognitionActivityService
{
    public partial class Service1 : ServiceBase
    {
        Timer timer = new Timer(); // name space(using System.Timers;)  
        const string FILEPATH = @"C:/log.xls";
        const int INTERVAL = 5000; //number in milisecinds  
        public Service1()
        {
            ParsePythonLogFile(FILEPATH);
            InitializeComponent();
        }

        protected override void OnStart(string[] args)
        {
            timer.Elapsed += new ElapsedEventHandler(OnElapsedTime);
            timer.Interval = INTERVAL;
            timer.Enabled = true;
        }

        private void OnElapsedTime(object source, ElapsedEventArgs e)
        {
            ParsePythonLogFile(FILEPATH);
        }

        protected override void OnStop()
        {
        }

        public void ParsePythonLogFile(string filePath)
        {
            using (StreamReader sr = new StreamReader(filePath))
            {
                string currentLine;
                string prevLine= null;
                int rowCount = 0;
                string[] prevLineColumns = null;
                // currentLine will be null when the StreamReader reaches the end of file
                while ((currentLine = sr.ReadLine()) != null)
                {
                    if(rowCount++==0) continue;
                    string[] currLineColumns = currentLine.Split('\t');
                    if (!string.IsNullOrEmpty(currLineColumns[1]))
                    {
                        prevLine = currentLine;
                        prevLineColumns = prevLine.Split('\t');
                        continue;
                    }

                    InsertInDatabse(prevLineColumns, currLineColumns);
                }
            }
        }

        private void InsertInDatabse(string[] prevLineColumns, string[] currLineColumns)
        {
            // create sql connection object.  Be sure to put a valid connection string
            SqlConnection Con = new SqlConnection("Data Source=localhost;Initial Catalog=Sparkthon;Integrated Security=SSPI;");
            // create command object with SQL query and link to connection object
            SqlCommand Cmd = new SqlCommand("INSERT INTO dbo.Crookie " +
                                            "(TimeIn, Name, X,Y,X2,Y2,TimeOut,Camera,DetectionScore) " +
                                            "VALUES(@TimeIn,@Name,@X,@Y,@X2,@Y2,@TimeOut,@Camera,@DetectionScore)", Con);

            // create your parameters
            Cmd.Parameters.Add("@TimeIn", System.Data.SqlDbType.DateTime);
            Cmd.Parameters.Add("@Name", System.Data.SqlDbType.NVarChar);
            Cmd.Parameters.Add("@X", System.Data.SqlDbType.Int);
            Cmd.Parameters.Add("@Y", System.Data.SqlDbType.Int);
            Cmd.Parameters.Add("@X2", System.Data.SqlDbType.Int);
            Cmd.Parameters.Add("@Y2", System.Data.SqlDbType.Int);
            Cmd.Parameters.Add("@TimeOut", System.Data.SqlDbType.DateTime);
            Cmd.Parameters.Add("@Camera", System.Data.SqlDbType.NVarChar);
            Cmd.Parameters.Add("@DetectionScore", System.Data.SqlDbType.NVarChar);
            // set values to parameters from arrays
            Cmd.Parameters["@TimeIn"].Value = DateTime.Parse(prevLineColumns[0]);
            Cmd.Parameters["@Name"].Value = prevLineColumns[1];
            var xyValues = ReturnImagePositions(prevLineColumns[2]);
            Cmd.Parameters["@X"].Value = Convert.ToInt32(xyValues[0]);
            Cmd.Parameters["@Y"].Value = Convert.ToInt32(xyValues[1]);
            Cmd.Parameters["@X2"].Value = Convert.ToInt32(xyValues[2]);
            Cmd.Parameters["@Y2"].Value = Convert.ToInt32(xyValues[3]);  
            Cmd.Parameters["@TimeOut"].Value = DateTime.Parse(currLineColumns[0]);
            Cmd.Parameters["@DetectionScore"].Value = currLineColumns[3];
            Cmd.Parameters["@Camera"].Value = prevLineColumns[4];
            
            // open sql connection
            Con.Open();

            // execute the query and return number of rows affected, should be one
            int RowsAffected = Cmd.ExecuteNonQuery();

            // close connection when done
            Con.Close();
        }

        private string[] ReturnImagePositions(string parameters)
        {
            return parameters.Remove(0, 1).Remove(18, 1).Split(',');
        }
    
    }
}
