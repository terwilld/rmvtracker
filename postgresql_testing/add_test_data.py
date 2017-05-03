#!/usr/bin/python2.4


ResultList=['27-04-2017', -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15]

import psycopg2
try:
    conn = psycopg2.connect("dbname='rmv_scraping' user='davidterwilliger' host='localhost' password=sadf")
    print '123'
    cur = conn.cursor()
    print '456'
    #cur.execute("CREATE TABLE Cars(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)")
    print '789'


    cur.execute("INSERT into Current_data_1(Date_time, \
        Attleboro_Licensing, Attleboro_Registration, \
        Boston_Licensing, Boston_Registration, \
        Braintree_Licensing, Braintree_Registration, \
        Brockton_Licensing, Brockton_Registration, \
        Chicopee_Licensing, Chicopee_Registration, \
        Easthampton_Licensing, Easthampton_Registration, \
        Fall_River_Licensing, Fall_River_Registration, \
        Greenfield_Licensing, Greenfield_Registration, \
        Haverhill_Licensing, Haverhill_Registration, \
        Lawrence_Licensing, Lawrence_Registration, \
        Leominster_Licensing, Leominster_Registration, \
        Lowell_Licensing, Lowell_Registration, \
        Marthas_Vineyard_Licensing, Marthas_Vineyard_Registration, \
        Milford_Licensing, Milford_Registration, \
        Nantucket_Licensing, Nantucket_Registration, \
        Natick_Licensing, Natick_Registration, \
        New_Bedford_Licensing, New_Bedford_Registration, \
        North_Adams_Licensing, North_Adams_Registration, \
        Pittsfield_Licensing, Pittsfield_Registration, \
        Plymouth_Licensing, Plymouth_Registration, \
        Revere_Licensing, Revere_Registration, \
        Roslindale_Licensing, Roslindale_Registration, \
        South_Yarmouth_Licensing, South_Yarmouth_Registration, \
        Springfield_Licensing, Springfield_Registration, \
        Taunton_Licensing, Taunton_Registration, \
        Watertown_Licensing, Watertown_Registration, \
        Wilmington_Licensing, Wilmington_Registration, \
        Worcester_Licensing, Worcester_Registration) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s)", ResultList)

#['27-04-2017', '22:13:55', -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15, -15]


    conn.commit()

except Exception, e:
    print "I am unable to connect to the database"
    print "Couldn't do it: %s" % e



finally:
    
    if conn:
        conn.close()
        print 'cloes'

print 'done'
