import arcpy

#Allow Python to overwrite existing files and data.
arcpy.env.overwriteOutput = True

#Create variables - some of these will be reused a lot.
platform = 'POSTGRESQL'
instance = '10.38.3.104'
#database = 'fdgdb_administration'
authentication = 'DATABASE_AUTH'
databaseAdmin = 'postgres' 
databaseAdminPass = 'DBDad67891$'
schema = 'SDE_SCHEMA'
gdbAdmin = 'sde'
adminPass = 'sdeDad67891$'
tablespace = ''
authFile = "D:\\Other\\FDGDB_Connections\\keycodes_2019"


databaseAdmin = gdbAdmin
databaseAdminPass = adminPass

import pandas as pd

myhtml = pd.read_html("D:\Other\FDGDB_Connections\FD_geodatabases.html")
#print(myhtml[0])
database_list= myhtml[0][0]

for database in database_list:
    connection_file_name = "sde@"+database+".sde"
    try:
    
        # Create Enterprise Geodatabase.
        #print("Creating the enterprise geodatabase")
        #arcpy.CreateEnterpriseGeodatabase_management(platform, instance, database,
                                                     #authentication, databaseAdmin,
                                                     #databaseAdminPass, schema, gdbAdmin,
                                                     #adminPass, tablespace, authFile)
    
        # Once the database has been created we will create an admin
        # connection so that we can create users in it.
        print("Creating connection to geodatabase as the SDE user")
        adminConn = arcpy.CreateDatabaseConnection_management('D:\Other\FDGDB_Connections',
                                                              connection_file_name, platform, instance, authentication,
                                                              databaseAdmin, databaseAdminPass,'SAVE_USERNAME', database)
        
        connection_file_name= 'D:\\Other\\FDGDB_Connections\\'+ connection_file_name
        
        UpdateEnterpriseGeodatabaseLicense_management (connection_file_name, authFile )
        
        print (database + " successfully license updated.")
    except:
        print( connection_file_name + "can not connected")
        