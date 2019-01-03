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
instance = '10.38.3.123'
database = 'versioning_training'
authentication = 'DATABASE_AUTH'
databaseAdmin = 'postgres' 
databaseAdminPass = 'postgres'
schema = 'SDE_SCHEMA'
gdbAdmin = 'sde'
adminPass = 'sdeDad67891$'
tablespace = ''
authFile = 'D:\CommonSharedFolder_TempOnly\DrMoeMyint\Required Tools for Arcgis server Geodatabase creation\ESRI_Servers\server123_keycodes\keycodes_20190519_OMMTEST'


try:

    # Create Enterprise Geodatabase.
    #print("Creating the enterprise geodatabase")
    #arcpy.CreateEnterpriseGeodatabase_management(platform, instance, database,
                                                 #authentication, databaseAdmin,
                                                 #databaseAdminPass, schema, gdbAdmin,
                                                 #adminPass, tablespace, authFile)

    # Once the database has been created we will create an admin
    # connection so that we can create users in it.
    print("Creating connection to geodatabase as the DBA user")
    adminConn = arcpy.CreateDatabaseConnection_management('D:/versioning_training',
                                                          'Admin@versioning_training.sde', platform, instance, authentication,
                                                          databaseAdmin, databaseAdminPass,'SAVE_USERNAME', database)


    # First create a few roles for data viewers and data editors.
    print("Creating the viewer and editor roles")
    arcpy.CreateRole_management(adminConn, 'viewers')
    arcpy.CreateRole_management(adminConn, 'editors')

    # Next create users and assign them to their proper roles.
    # Generate a list of users to be added as editors and a list to be added as viewers.
    print("Creating users")
    onemap_editors = ['onemap_editor1', 'onemap_editor2', 'onemap_editor3', 'onemap_editor4', 'onemap_editor5', 'onemap_editor6', 'onemap_editor7', 'onemap_editor8', 'onemap_editor9', 'onemap_editor10', 'onemap_editor11', 'onemap_editor12', 'onemap_editor13', 'onemap_editor14', 'onemap_editor15', 'onemap_editor16', 'onemap_editor17', 'onemap_editor18', 'onemap_editor19', 'onemap_editor20']
    onemap_viewers = ['onemap_viewer1', 'onemap_viewer2', 'onemap_viewer3', 'onemap_viewer4', 'onemap_viewer5','onemap_viewer6', 'onemap_viewer7', 'onemap_viewer8', 'onemap_viewer9', 'onemap_viewer10', 'onemap_viewer11', 'onemap_viewer12', 'onemap_viewer13', 'onemap_viewer14','onemap_viewer15', 'onemap_viewer16', 'onemap_viewer17', 'onemap_viewer18', 'onemap_viewer19', 'onemap_viewer20']

    for user in editors:
        arcpy.CreateDatabaseUser_management(adminConn, 'DATABASE_USER',
                                            user, user, 'editors')
    for user1 in viewers:
        arcpy.CreateDatabaseUser_management(adminConn, 'DATABASE_USER',
                                            user1, user1, 'viewers')

    # Create a data owner user named 'gdb'
    print("Creating the data owner (onemapgdb_owner)")
    arcpy.CreateDatabaseUser_management(adminConn, 'DATABASE_USER', 'onemapgdb_owner', 'onemapgdb_owner')
    print("Finished tasks as the DBA user \n")
    
    # Now connect as the gdb admin to import a custom configuration keyword
    print("Creating a connection to the geodatabase as the gdb admin user (sde)")
    gdbAdminConn = arcpy.CreateDatabaseConnection_management('D:/versioning_training',
                                                          'sde@versioning_training.sde', platform, instance,
                                                          'DATABASE_AUTH', gdbAdmin, adminPass,
                                                          'SAVE_USERNAME', database)
    
    # Import a custom configuration keyword for the data owner to use
    # The file being imported had been exported from dbtune, modified, and now ready to import
    #print("Import a new geodatabase configuration keyword named 'custom'")
    #arcpy.ImportGeodatabaseConfigurationKeywords_management(gdbAdminConn,  r'C:\presentations\DevSummit2016\Demos\Demo3\CustomConfigKeyword')
    #print("Finished tasks as the gdb admin user (sde) \n")
    
    # Create schema and apply permissions.
    # Create a connection as the data owner.
    print("Creating a connection to the geodatabase as the data owner (onemapgdb_owner)")
    ownerConn = arcpy.CreateDatabaseConnection_management('D:/versioning_training',
                                                          'onemapgdb_owner@versioning.sde', platform, instance,
                                                          'DATABASE_AUTH', 'onemapgdb_owner','onemapgdb_owner',
                                                          'SAVE_USERNAME', database)
    
    # Import the data as the gdb user and specify the custom config keyword that the gdb admin has provided
    print("Importing the data as the data owner (onemapgdb_owner) using a default config keyword named 'default'")
    arcpy.ImportXMLWorkspaceDocument_management(ownerConn,
                                                '//OMM-W20/CommonSharedFolder_TempOnly/Script_for_OMMtest_DB',
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




