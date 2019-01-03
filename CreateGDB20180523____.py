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
database = 'CompleteUserDB'
authentication = 'DATABASE_AUTH' #'OPERATING_SYSTEM_AUTH'
databaseAdmin = 'postgres' #SA
databaseAdminPass = 'DBDad67891$'
schema = 'SDE_SCHEMA'
gdbAdmin = 'sde'
adminPass = 'sdeDad67891$'
tablespace = ''
authFile = 'D:\ArcGISServerLic\keycodes'
databaseFolderConnecton = 'D:\SoeMyatMin\CompleteUser'

try:
    # Create Enterprise Geodatabase.
    print("Creating the enterprise geodatabase")
    arcpy.CreateEnterpriseGeodatabase_management(platform, instance, database,
                                                 authentication, databaseAdmin,
                                                 databaseAdminPass, schema, gdbAdmin,
                                                 adminPass, tablespace, authFile)

    # Once the database has been created we will create an admin
    # connection so that we can create users in it.
    print("Creating connection to geodatabase as the DBA user")
    adminConn = arcpy.CreateDatabaseConnection_management(databaseFolderConnecton,
                                                          'sde@CompleteUserDB_TuDell.sde', platform, instance, authentication,
                                                          gdbAdmin,adminPass,'SAVE_USERNAME', database)


    # First create a few roles for data viewers and data editors.
    print("Creating the viewer and editor roles")
    arcpy.CreateRole_management(adminConn, 'viewers')
    arcpy.CreateRole_management(adminConn, 'editors')

    # Next create users and assign them to their proper roles.
    # Generate a list of users to be added as editors and a list to be added as viewers.
    print("Creating users")
    #editors = ['matt', 'colin', 'andrew', 'gary']

    fd_editors = ['fd_editor1', 'fd_editor2', 'fd_editor3', 'fd_editor4', 'fd_editor5', 'fd_editor6', 'fd_editor7', 'fd_editor8', 'fd_editor9', 'fd_editor10', 'fd_editor11', 'fd_editor12', 'fd_editor13', 'fd_editor14', 'fd_editor15', 'fd_editor16', 'fd_editor17', 'fd_editor18', 'fd_editor19', 'fd_editor20']

    for user in fd_editors:
        arcpy.CreateDatabaseUser_management(adminConn, 'DATABASE_USER',
                                            user, user, 'editors')    
    
    #viewers = ['heather', 'jon', 'annie', 'shawn']
    viewers = []
    
    fd_viewers = ['fd_viewer1', 'fd_viewer2', 'fd_viewer3', 'fd_viewer4', 'fd_viewer5','fd_viewer6', 'fd_viewer7', 'fd_viewer8', 'fd_viewer9', 'fd_viewer10', 'fd_viewer11', 'fd_viewer12', 'fd_viewer13', 'fd_viewer14','fd_viewer15', 'fd_viewer16', 'fd_viewer17', 'fd_viewer18', 'fd_viewer19', 'fd_viewer20']
    viewers.extend(fd_viewers)
    
    fd_dfo_editors = ['fd_Hinthada_editor1',on_West_editor5','fd_Yangon_West_editor6','fd_Yangon_West_editor7','fd_Yangon_West_editor8','fd_Yangon_West_editor9']    

    viewers.extend(fd_dfo_editors)

    fd_dfo_viewers = ['fd_Hinthada_viewer1','fd_Hinthada_viewer2',fd_Yangon_West_viewer8','fd_Yangon_West_viewer9']    
          

    viewers.extend(fd_dfo_viewers)   
            
            
    agri_editors = ['agri_editor1', 'agri_editor2', 'agri_editor3', 'agri_editor4', 'agri_editor5', 'agri_editor6', 'agri_editor7', 'agri_editor8', 'agri_editor9', 'agri_editor10', 'agri_editor11', 'agri_editor12', 'agri_editor13', 'agri_editor14', 'agri_editor15', 'agri_editor16', 'agri_editor17', 'agri_editor18', 'agri_editor19', 'agri_editor20']
    viewers.extend(agri_editors)    
    
    agri_viewers = ['agri_viewer1', 'agri_viewer2', 'agri_viewer3', 'agri_viewer4', 'agri_viewer5','agri_viewer6', 'agri_viewer7', 'agri_viewer8', 'agri_viewer9', 'agri_viewer10', 'agri_viewer11', 'agri_viewer12', 'agri_viewer13', 'agri_viewer14','agri_viewer15', 'agri_viewer16', 'agri_viewer17', 'agri_viewer18', 'agri_viewer19', 'agri_viewer20']            
    viewers.extend(agri_viewers)
    
    onemap_editors = ['onemap_editor1', 'onemap_editor2', 'onemap_editor3', 'onemap_editor4', 'onemap_editor5', 'onemap_editor6', 'onemap_editor7', 'onemap_editor8', 'onemap_editor9', 'onemap_editor10', 'onemap_editor11', 'onemap_editor12', 'onemap_editor13', 'onemap_editor14', 'onemap_editor15', 'onemap_editor16', 'onemap_editor17', 'onemap_editor18', 'onemap_editor19', 'onemap_editor20']
    viewers.extend(onemap_editors)
       
    onemap_viewers = ['onemap_viewer1', 'onemap_viewer2', 'onemap_viewer3', 'onemap_viewer4', 'onemap_viewer5','onemap_viewer6', 'onemap_viewer7', 'onemap_viewer8', 'onemap_viewer9', 'onemap_viewer10', 'onemap_viewer11', 'onemap_viewer12', 'onemap_viewer13', 'onemap_viewer14','onemap_viewer15', 'onemap_viewer16', 'onemap_viewer17', 'onemap_viewer18', 'onemap_viewer19', 'onemap_viewer20']            
    viewers.extend(onemap_viewers)
                          
    landcore_editors = ['landcore_editor1', 'landcore_editor2', 'landcore_editor3', 'landcore_editor4', 'landcore_editor5', 'landcore_editor6', 'landcore_editor7', 'landcore_editor8', 'landcore_editor9', 'landcore_editor10', 'landcore_editor11', 'landcore_editor12', 'landcore_editor13', 'landcore_editor14', 'landcore_editor15', 'landcore_editor16', 'landcore_editor17', 'landcore_editor18', 'landcore_editor19', 'landcore_editor20']
    viewers.extend(landcore_editors)

    landcore_viewers = ['landcore_viewer1', 'landcore_viewer2', 'landcore_viewer3', 'landcore_viewer4', 'landcore_viewer5','landcore_viewer6', 'landcore_viewer7', 'landcore_viewer8', 'landcore_viewer9', 'landcore_viewer10', 'landcore_viewer11', 'landcore_viewer12', 'landcore_viewer13', 'landcore_viewer14','landcore_viewer15', 'landcore_viewer16', 'landcore_viewer17', 'landcore_viewer18', 'landcore_viewer19', 'landcore_viewer20']            
    viewers.extend(landcore_viewers)
                                               
    publisher_editors = ['publisher_editor1', 'publisher_editor2', 'publisher_editor3', 'publisher_editor4', 'publisher_editor5', 'publisher_editor6', 'publisher_editor7', 'publisher_editor8', 'publisher_editor9', 'publisher_editor10', 'publisher_editor11', 'publisher_editor12', 'publisher_editor13', 'publisher_editor14', 'publisher_editor15', 'publisher_editor16', 'publisher_editor17', 'publisher_editor18', 'publisher_editor19', 'publisher_editor20']
    viewers.extend(publisher_editors)
    
    publisher_viewers = ['publisher_viewer1', 'publisher_viewer2', 'publisher_viewer3', 'publisher_viewer4', 'publisher_viewer5','publisher_viewer6', 'publisher_viewer7', 'publisher_viewer8', 'publisher_viewer9', 'publisher_viewer10', 'publisher_viewer11', 'publisher_viewer12', 'publisher_viewer13', 'publisher_viewer14','publisher_viewer15', 'publisher_viewer16', 'publisher_viewer17', 'publisher_viewer18', 'publisher_viewer19', 'publisher_viewer20']            
    viewers.extend(publisher_viewers)
    
    qc_editors = ['qc_editor1', 'qc_editor2', 'qc_editor3', 'qc_editor4', 'qc_editor5', 'qc_editor6', 'qc_editor7', 'qc_editor8', 'qc_editor9', 'qc_editor10', 'qc_editor11', 'qc_editor12', 'qc_editor13', 'qc_editor14', 'qc_editor15', 'qc_editor16', 'qc_editor17', 'qc_editor18', 'qc_editor19', 'qc_editor20']
    viewers.extend(qc_editors)
        
    qc_viewers = ['qc_viewer1', 'qc_viewer2', 'qc_viewer3', 'qc_viewer4', 'qc_viewer5','qc_viewer6', 'qc_viewer7', 'qc_viewer8', 'qc_viewer9', 'qc_viewer10', 'qc_viewer11', 'qc_viewer12', 'qc_viewer13', 'qc_viewer14','qc_viewer15', 'qc_viewer16', 'qc_viewer17', 'qc_viewer18', 'qc_viewer19', 'qc_viewer20']            
    viewers.extend(qc_viewers)
        
    mern_editors = ['mern_editor1', 'mern_editor2', 'mern_editor3', 'mern_editor4', 'mern_editor5', 'mern_editor6', 'mern_editor7', 'mern_editor8', 'mern_editor9', 'mern_editor10', 'mern_editor11', 'mern_editor12', 'mern_editor13', 'mern_editor14', 'mern_editor15', 'mern_editor16', 'mern_editor17', 'mern_editor18', 'mern_editor19', 'mern_editor20']
    viewers.extend(mern_editors)
    
    mern_viewers = ['mern_viewer1', 'mern_viewer2', 'mern_viewer3', 'mern_viewer4', 'mern_viewer5','mern_viewer6', 'mern_viewer7', 'mern_viewer8', 'mern_viewer9', 'mern_viewer10', 'mern_viewer11', 'mern_viewer12', 'mern_viewer13', 'mern_viewer14','mern_viewer15', 'mern_viewer16', 'mern_viewer17', 'mern_viewer18', 'mern_viewer19', 'mern_viewer20']          
    viewers.extend(mern_viewers)
       
    for user1 in viewers:
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
    
    # Import the data as the gdb user and specify the custom config keyword that the gdb admin has provided
    print("Importing the data as the data owner (gdb) using a default config keyword ")
    arcpy.ImportXMLWorkspaceDocument_management(ownerConn,
                                                'D:\Presentations\data\XMLEXPORT_MYANMAR_DATA.xml',
                                                'DATA')

    # Get a list of feature classes, tables and feature datasets
    # and apply appropriate permissions.
    print("Building a list of feature classes, tables, and feature datasets in the geodatabase")
    arcpy.env.workspace = ownerConn[0] #note environments do not work with result objects.
    dataList = arcpy.ListTables() + arcpy.ListFeatureClasses() + arcpy.ListDatasets("", "Feature")

    # Use roles to apply permissions.
    print("Granting appropriate privileges to the data for the 'viewers' and 'editors' roles")
    arcpy.ChangePrivileges_management(dataList, 'viewers', 'GRANT')
    arcpy.ChangePrivileges_management(dataList, 'editors', 'GRANT', 'GRANT')

    # Register the data as versioned.
    print("Registering the data as versioned")
    for dataset in dataList:
        arcpy.RegisterAsVersioned_management(dataset)

    # Finally, create a version for each editor.
    print("Creating a private version for each user in the editor role")
    for user3 in fd_editors:
        verCreateConn = arcpy.CreateDatabaseConnection_management(databaseFolderConnecton,
                                                                  'DSVersionCreate.sde', platform, instance,
                                                                  'DATABASE_AUTH', user3,
                                                                  user3,'SAVE_USERNAME',
                                                                  database)
        arcpy.CreateVersion_management(verCreateConn, 'sde.DEFAULT',
                                       user3 + '_EditVersion', 'PRIVATE')
        arcpy.ClearWorkspaceCache_management()
    print('Done')
except:
    print('Script failure.\n')
    print(arcpy.GetMessages())



