from apscheduler.schedulers.blocking import BlockingScheduler

from scrape_locations import *
import psycopg2,urlparse
from subprocess import Popen, PIPE


sched = BlockingScheduler()


	#Gather DB credentials
try:
    print 'no config imported: this is a deployed build'
    urlparse.uses_netloc.append("postgres")
    url = urlparse.urlparse(os.environ["DATABASE_URL"])
    DB_name = url.path[1:]
    DB_user = url.username
    DB_password = url.password
    DB_host = url.hostname
    DB_port = url.port
    print '<clocks.py not inside local test> DB_name: ', DB_name
    print '<clocks.py not inside local test> DB_user: ', DB_user
    print '<clocks.py not inside local test> DB_password: ', DB_password
    print '<clocks.py not inside local test> DB_host: ', DB_host
    print '<clocks.py not inside local test> DB_port: ', DB_port
    print 'database type : ', type(url.path[1:]), ' Database name: ', str(url.path[1:])
    print 'user type : ', type(url.username), ' User:  ', str(url.username)
    print 'password type: ', type(url.password), ' Password: ', str(url.password)
    print 'host type : ', type (url.hostname), ' Host: ', str(url.hostname)
    print 'port type: ', type(url.port), ' Port: ', str(url.port)

except:
	print 'clocks data base credentials failed to gather'








# @sched.scheduled_job('interval', minutes=3)
# def timed_job():
#     print('This job is run every three minutes.')

@sched.scheduled_job('cron', day_of_week='mon-fri', hour='6-22', minute='*/3')
def scheduled_job_1():
    print('This job is run every weekday every 3 minutes with the hour addition.')


print 'test_1_!_1'
@sched.scheduled_job('cron', day_of_week='mon-fri', minute='*/10')
def scheduled_job():
    print('This job is run every weekday every 3 minutes without the hour addition.')
    print '123432123'
    #Result_List=add_a_reading(list_of_towns)
    #print Result_List
    list_of_towns=['Attleboro','Boston','Braintree','Brockton','Chicopee','Easthampton','Fall%20River','Greenfield','Haverhill','Lawrence','Leominster','Lowell','Martha%27s%20Vineyard','Milford','Nantucket','Natick','New%20Bedford','North%20Adams','Pittsfield','Plymouth','Revere','Roslindale','South%20Yarmouth','Springfield','Taunton','Watertown','Wilmington','Worcester']
    Result_List=add_a_reading(list_of_towns)
    print Result_List
    print 'test'

    print 'test'
    conn = psycopg2.connect(database=DB_name,user=DB_user,password=DB_password,host=DB_host,port=DB_port,sslmode='require')
    print 'made connection'
    cur = conn.cursor()
    print 'about to try and place in the database'

    cur.execute("INSERT into Current_data(Date_time, \
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
        Worcester_Licensing, Worcester_Registration) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s)", Result_List)
    print'may have actually put into the database'
    conn.commit()
    conn.close()



print 'test_2_@_2_2_@'

sched.start()


