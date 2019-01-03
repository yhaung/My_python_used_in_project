# Name: CreateGDB.py
# Description: This script will create an enterprise geodatabase,
#              create schema, users, roles, and versions. It will
#              also apply permissions to all data. The end result
#              is a geodatabase that is ready to use.
# Author: Esri

import arcpy

#Allow Python to overwrite existing files and data.
arcpy.env.overwriteOutput = True

#Create variables - some of these will be reused a lot.
platform = 'POSTGRESQL'
instance = '10.38.3.104'
database = 'yee'
authentication = 'DATABASE_AUTH'
databaseAdmin = 'postgres' 
databaseAdminPass = 'DBDad67891$'
schema = 'SDE_SCHEMA'
gdbAdmin = 'sde'
adminPass = 'sdeDad67891$'
tablespace = ''
authFile = 'D:\ArcSWAT_training\FD_Presentation\KNWLicense\keycodes'


try:

    # Create Enterprise Geodatabase.
    #print("Creating the enterprise geodatabase")
    #arcpy.CreateEnterpriseGeodatabase_management(platform, instance, database,
    #                                             authentication, databaseAdmin,
    #                                             databaseAdminPass, schema, gdbAdmin,
    #                                             adminPass, tablespace, authFile)

    # Once the database has been created we will create an admin
    # connection so that we can create users in it.
    print("Creating connection to geodatabase as the DBA user")
    adminConn = arcpy.CreateDatabaseConnection_management('D:/FD/yee'
                                                          'DevSumAdmin.sde', platform, instance, authentication,
                                                          databaseAdmin, databaseAdminPass,'SAVE_USERNAME', database)


    # First create a few roles for data viewers and data editors.
    print("Creating the viewer and editor roles")
    arcpy.CreateRole_management(adminConn, 'viewers')
    arcpy.CreateRole_management(adminConn, 'editors')

    # Next create users and assign them to their proper roles.
    # Generate a list of users to be added as editors and a list to be added as viewers.
    print("Creating users")
    fd_editors = ['fd_editor1', 'fd_editor2', 'fd_editor3', 'fd_editor4', 'fd_editor5', 'fd_editor6', 'fd_editor7', 'fd_editor8', 'fd_editor9', 'fd_editor10', 'fd_editor11', 'fd_editor12', 'fd_editor13', 'fd_editor14', 'fd_editor15', 'fd_editor16', 'fd_editor17', 'fd_editor18', 'fd_editor19', 'fd_editor20']
    fd_viewers = ['fd_viewer1', 'fd_viewer2', 'fd_viewer3', 'fd_viewer4', 'fd_viewer5','fd_viewer6', 'fd_viewer7', 'fd_viewer8', 'fd_viewer9', 'fd_viewer10', 'fd_viewer11', 'fd_viewer12', 'fd_viewer13', 'fd_viewer14','fd_viewer15', 'fd_viewer16', 'fd_viewer17', 'fd_viewer18', 'fd_viewer19', 'fd_viewer20']
    for user in editors:
        arcpy.CreateDatabaseUser_management(adminConn, 'DATABASE_USER',
                                            user, user, 'editors')
    for user1 in viewers:
        arcpy.CreateDatabaseUser_management(adminConn, 'DATABASE_USER',
                                            user1, user1, 'viewers')

    # Create a data owner user named 'gdb'
    print("Creating the data owner (fdgdb_owner)")
    arcpy.CreateDatabaseUser_management(adminConn, 'DATABASE_USER', 'fdgdb_owner', 'fdgdb_owner')
    print("Finished tasks as the DBA user \n")
    
    # Now connect as the gdb admin to import a custom configuration keyword
    print("Creating a connection to the geodatabase as the gdb admin user (sde)")
    gdbAdminConn = arcpy.CreateDatabaseConnection_management('D:/FD/yee',
                                                          'gdbAdmin.sde', platform, instance,
                                                          'DATABASE_AUTH', gdbAdmin, adminPass,
                                                          'SAVE_USERNAME', database)
    
    # Import a custom configuration keyword for the data owner to use
    # The file being imported had been exported from dbtune, modified, and now ready to import
    #print("Import a new geodatabase configuration keyword named 'custom'")
    #arcpy.ImportGeodatabaseConfigurationKeywords_management(gdbAdminConn,  r'C:\presentations\DevSummit2016\Demos\Demo3\CustomConfigKeyword')
    #print("Finished tasks as the gdb admin user (sde) \n")
    
    # Create schema and apply permissions.
    # Create a connection as the data owner.
    print("Creating a connection to the geodatabase as the data owner (fdgdb_owner)")
    ownerConn = arcpy.CreateDatabaseConnection_management('D:/FD/yee',
                                                          'DevSumOwner.sde', platform, instance,
                                                          'DATABASE_AUTH', 'fdgdb_owner','fdgdb_owner',
                                                          'SAVE_USERNAME', database)
    
    # Import the data as the gdb user and specify the custom config keyword that the gdb admin has provided
    print("Importing the data as the data owner (fdgdb_owner) using a default config keyword named 'default'")
    arcpy.ImportXMLWorkspaceDocument_management(ownerConn,
                                                'E:/FD_Presentation/data/EXAMPLEDATAVERSIONING.XML',
                                                'DATA')

    # Get a list of feature classes, tables and feature datasets
    # and apply appropriate permissions.
    print("Building a list of feature classes, tables, and feature datasets in the geodatabase")
    arcpy.env.workspace = ownerConn[0] #note environments do not work with result objects.
    dataList = arcpy.ListTables() + arcpy.ListFeatureClasses() + arcpy.ListDatasets("", "Feature")
    
    #List the data in the dataList
    print("Print the list of dataset")
    for dataset in dataList:
        print(dataset)

    # Use roles to apply permissions.
    print("Granting appropriate privileges to the data for the 'viewers' and 'editors' roles")
    arcpy.ChangePrivileges_management(dataList, 'viewers', 'GRANT')
    arcpy.ChangePrivileges_management(dataList, 'editors', 'GRANT', 'GRANT')

    # Register the data as versioned.
    print("Registering the data as versioned")
    for dataset in dataList:
        arcpy.RegisterAsVersioned_management(dataset)
        
        

    # Finally, create a version for each editor.
    #print("Creating a private version for each user in the editor role")
    #for user3 in editors:
    #    verCreateConn = arcpy.CreateDatabaseConnection_management('C:/presentations/DevSummit2016/Demos/Demo3',
    #                                                              'DSVersionCreate.sde', platform, instance,
    #                                                              'DATABASE_AUTH', user3,
    #                                                              user3,'SAVE_USERNAME',
    #                                                              database)
    #    arcpy.CreateVersion_management(verCreateConn, 'sde.DEFAULT',
    #                                   user3 + '_EditVersion', 'PRIVATE')
    #    arcpy.ClearWorkspaceCache_management()
    #print('Done')

except:
    print('Script failure.\n')
    print(arcpy.GetMessages())




