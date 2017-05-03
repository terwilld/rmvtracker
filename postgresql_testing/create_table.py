#!/usr/bin/python2.4
# Small script to show PostgreSQL and Pyscopg together
import psycopg2
try:
    conn = psycopg2.connect("dbname='rmv_scraping' user='davidterwilliger' host='localhost' password=sadf")
    print '123'
    cur = conn.cursor()
    print '456'
    #cur.execute("CREATE TABLE Cars(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)")
    print '789'
    cur.execute("CREATE TABLE Current_Data(Date VARCHAR(20), Time VARCHAR(20), \
        Attleboro_Licensing INT, Attleboro_Registration INT, \
        Boston_Licensing INT, Boston_Registration INT, \
        Braintree_Licensing INT, Braintree_Registration INT, \
        Brockton_Licensing INT, Brockton_Registration INT, \
        Chicopee_Licensing INT, Chicopee_Registration INT, \
        Easthampton_Licensing INT, Easthampton_Registration INT, \
        Fall_River_Licensing INT, Fall_River_Registration INT, \
        Greenfield_Licensing INT, Greenfield_Registration INT, \
        Haverhill_Licensing INT, Haverhill_Registration INT, \
        Lawrence_Licensing INT, Lawrence_Registration INT, \
        Leominster_Licensing INT, Leominster_Registration INT, \
        Lowell_Licensing INT, Lowell_Registration INT, \
        Marthas_Vineyard_Licensing INT, Marthas_Vineyard_Registration INT, \
        Milford_Licensing INT, Milford_Registration INT, \
        Nantucket_Licensing INT, Nantucket_Registration INT, \
        Natick_Licensing INT, Natick_Registration INT, \
        New_Bedford_Licensing INT, New_Bedford_Registration INT, \
        North_Adams_Licensing INT, North_Adams_Registration INT, \
        Pittsfield_Licensing INT, Pittsfield_Registration INT, \
        Plymouth_Licensing INT, Plymouth_Registration INT, \
        Revere_Licensing INT, Revere_Registration INT, \
        Roslindale_Licensing INT, Roslindale_Registration INT, \
        South_Yarmouth_Licensing INT, South_Yarmouth_Registration INT, \
        Springfield_Licensing INT, Springfield_Registration INT, \
        Taunton_Licensing INT, Taunton_Registration INT, \
        Watertown_Licensing INT, Watertown_Registration INT, \
        Wilmington_Licensing INT, Wilmington_Registration INT, \
        Worcester_Licensing INT, Worcester_Registration INT)")



    cur.execute("CREATE TABLE Current_Data_1(Date_time VARCHAR(35),\
        Attleboro_Licensing INT, Attleboro_Registration INT, \
        Boston_Licensing INT, Boston_Registration INT, \
        Braintree_Licensing INT, Braintree_Registration INT, \
        Brockton_Licensing INT, Brockton_Registration INT, \
        Chicopee_Licensing INT, Chicopee_Registration INT, \
        Easthampton_Licensing INT, Easthampton_Registration INT, \
        Fall_River_Licensing INT, Fall_River_Registration INT, \
        Greenfield_Licensing INT, Greenfield_Registration INT, \
        Haverhill_Licensing INT, Haverhill_Registration INT, \
        Lawrence_Licensing INT, Lawrence_Registration INT, \
        Leominster_Licensing INT, Leominster_Registration INT, \
        Lowell_Licensing INT, Lowell_Registration INT, \
        Marthas_Vineyard_Licensing INT, Marthas_Vineyard_Registration INT, \
        Milford_Licensing INT, Milford_Registration INT, \
        Nantucket_Licensing INT, Nantucket_Registration INT, \
        Natick_Licensing INT, Natick_Registration INT, \
        New_Bedford_Licensing INT, New_Bedford_Registration INT, \
        North_Adams_Licensing INT, North_Adams_Registration INT, \
        Pittsfield_Licensing INT, Pittsfield_Registration INT, \
        Plymouth_Licensing INT, Plymouth_Registration INT, \
        Revere_Licensing INT, Revere_Registration INT, \
        Roslindale_Licensing INT, Roslindale_Registration INT, \
        South_Yarmouth_Licensing INT, South_Yarmouth_Registration INT, \
        Springfield_Licensing INT, Springfield_Registration INT, \
        Taunton_Licensing INT, Taunton_Registration INT, \
        Watertown_Licensing INT, Watertown_Registration INT, \
        Wilmington_Licensing INT, Wilmington_Registration INT, \
        Worcester_Licensing INT, Worcester_Registration INT)")
    conn.commit()

except Exception, e:
    print "I am unable to connect to the database"
    print "Couldn't do it: %s" % e


finally:
    
    if conn:
        conn.close()



    #pg_ctl -D /usr/local/var/postgres start && brew services start postgresql
    	#awesome tutorial
#		https://www.codementor.io/devops/tutorial/getting-started-postgresql-server-mac-osx
    #CREATE DATABASE super_awesome_application;
    #GRANT ALL PRIVILEGES ON DATABASE super_awesome_application TO patrick;
#\q quits when in terminal  


#SELECT * FROM "default_msg_details";
# this tells you what's in a table






        ##      Helpful commands
        ##      psql                login
        ##      \du                 lists user accounts
        ##      \list               lists databases        
        ##      \dt                 lists tables
        ##      \connect (data base)    connects to the target database
        ##      create database 'name'  create database
        ##      drop database 'name'    deletes database
        ##      SELECT * FROM 'table name';     shows contents of the table
        ##      \q quits when in terminal  

