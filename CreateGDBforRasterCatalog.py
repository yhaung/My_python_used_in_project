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
database = 'mmrtopography'
authentication = 'DATABASE_AUTH' #'OPERATING_SYSTEM_AUTH'
databaseAdmin = 'postgres' #SA
databaseAdminPass = 'DBDad67891$'
schema = 'SDE_SCHEMA'
gdbAdmin = 'sde'
adminPass = 'sdeDad67891$'
tablespace = ''
authFile = 'D:\ArcGISServerLic\keycodes'
databaseFolderConnecton = 'D:\Presentations\RasterCatalog'

try:

    print("Creating connection to geodatabase as the DBA user")
    adminConn = arcpy.CreateDatabaseConnection_management(databaseFolderConnecton,
                                                          'sde@mmrtopography_TuDell.sde', platform, instance, authentication,
                                                          gdbAdmin,adminPass,'SAVE_USERNAME', database)   

    # First create a few roles for data viewers and data editors.
    print("Creating the viewer and editor roles")
    arcpy.CreateRole_management(adminConn, 'viewers')
    arcpy.CreateRole_management(adminConn, 'editors')

    # Next create users and assign them to their proper roles.
    # Generate a list of users to be added as editors and a list to be added as viewers.
    print("Creating users")
    
    onemap_editors = ['onemap_editor1', 'onemap_editor2', 'onemap_editor3', 'onemap_editor4', 'onemap_editor5', 'onemap_editor6', 'onemap_editor7', 'onemap_editor8', 'onemap_editor9', 'onemap_editor10', 'onemap_editor11', 'onemap_editor12', 'onemap_editor13', 'onemap_editor14', 'onemap_editor15', 'onemap_editor16', 'onemap_editor17', 'onemap_editor18', 'onemap_editor19', 'onemap_editor20']
    
    for user in onemap_editors:
        arcpy.CreateDatabaseUser_management(adminConn, 'DATABASE_USER',
                                            user, user, 'editors')    
           
    onemap_viewers = ['onemap_viewer1', 'onemap_viewer2', 'onemap_viewer3', 'onemap_viewer4', 'onemap_viewer5','onemap_viewer6', 'onemap_viewer7', 'onemap_viewer8', 'onemap_viewer9', 'onemap_viewer10', 'onemap_viewer11', 'onemap_viewer12', 'onemap_viewer13', 'onemap_viewer14','onemap_viewer15', 'onemap_viewer16', 'onemap_viewer17', 'onemap_viewer18', 'onemap_viewer19', 'onemap_viewer20']            
    
    for user1 in onemap_viewers:
        arcpy.CreateDatabaseUser_management(adminConn, 'DATABASE_USER',
                                            user1, user1, 'viewers')  
    
              

    # Create a data owner user named 'gdb'
    print("Creating the data owner (gdb)")
    arcpy.CreateDatabaseUser_management(adminConn, 'DATABASE_USER', 'gdb', 'gdb')
    print("Finished tasks as the DBA user \n")
    
    # Now connect as the gdb admin to import a custom configuration keyword
    print("Creating a connection to the geodatabase as the gdb admin user (sde)")
    gdbAdminConn = arcpy.CreateDatabaseConnection_management(databaseFolderConnecton,
                                                          'gdbAdmin.sde', platform, instance,
                                                          'DATABASE_AUTH', gdbAdmin, adminPass,
                                                          'SAVE_USERNAME', database)
    
    # Import a custom configuration keyword for the data owner to use
    # The file being imported had been exported from dbtune, modified, and now ready to import
    #print("Import a new geodatabase configuration keyword named 'custom'")
    #arcpy.ImportGeodatabaseConfigurationKeywords_management(gdbAdminConn,  r'C:\presentations\DevSummit2017\Demos\Demo3\CustomConfigKeyword')
    print("Finished tasks as the gdb admin user (sde) \n")
    
    # Create schema and apply permissions.
    # Create a connection as the data owner.
    print("Creating a connection to the geodatabase as the data owner (gdb)")
    ownerConn = arcpy.CreateDatabaseConnection_management(databaseFolderConnecton,
                                                          'DevSumOwner.sde', platform, instance,
                                                          'DATABASE_AUTH', 'gdb','gdb',
                                                          'SAVE_USERNAME', database)
    
    print('Done')
except:
    print('Script failure.\n')
    print(arcpy.GetMessages())



