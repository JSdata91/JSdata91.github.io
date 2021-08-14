# DataSci Python Project

Created by: John Shumway

Last Updated: 08/01/2021

=====================================
## <b>SETUP:</b>
  First you will need the latest version of Python (currenlty 3.7 as of this project). Once installed, you then need to get the modules "pymysql" and "matplotlib" and place them in a directory, and add the directory to your PYPATH.  Note that this project used Anaconda3 and Spyder tools to build and develop in. It isn't necessary to use those tools, but it will make installation easier.

  The database should be using mySQL (as the CRUD interface uses the pymysql module to interact). Load the data using an import feature.  You can also customize the data, as long as it follows the same format as the original data. 
  
### <b>pymysql: </b>  
Can install either at https://pypi.org/project/PyMySQL/ or using pip install pymysql (recommended)
### <b>matplotlib: </b> 
Can install at https://matplotlib.org/stable/users/installing.html
### <b>Anaconda 3:</b> 
If you want to use the Anaconda 3 package (which contains Spyder), you can get it at https://www.anaconda.com/


## TO USE:
  Run the Main.py script which will load the modules. The user will be provided a list of all modules currently available and can select from the list. Then, a 'Group ID' value will be requested for database uploads.  This value can be any combination of numbers and letters. 

 Independent modules will generate a single graph and save the file into 'Charts' and add the file to the database with that ID.

 Running All modules will generate multiple graphs under the same group ID.

 When looking to retreive a graph from the database, the user enters the group ID used to store it and will be presented with a list of charts to select from.
