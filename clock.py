from apscheduler.schedulers.blocking import BlockingScheduler

from scrape_locations import *
import psycopg2,urlparse
from subprocess import Popen, PIPE


sched = BlockingScheduler()




#nine_hours_from_now = datetime.now() + timedelta(hours=9)
tz = timezone('EST')
date_time=datetime.now(tz)
print 'with out adjustment'
print date_time

date_time=datetime.now(tz)+ timedelta(hours=1)
print 'with adjustment'
print date_time
date_time=date_time.isoformat()
print 'Date time with timezone specified: ' + date_time  
date_time=datetime.now().isoformat()
print 'Date time without timezone specified: ' + date_time 

	#Gather DB credentials 
try:

    print 'clocks.py: no config imported: this is a deployed build'
    urlparse.uses_netloc.append("postgres")
    url = urlparse.urlparse(os.environ["DATABASE_URL"])
    DB_name = url.path[1:]
    DB_user = url.username
    DB_password = url.password
    DB_host = url.hostname
    DB_port = url.port
    # print '<clocks.py not inside local test> DB_name: ', DB_name
    # print '<clocks.py not inside local test> DB_user: ', DB_user
    # print '<clocks.py not inside local test> DB_password: ', DB_password
    # print '<clocks.py not inside local test> DB_host: ', DB_host
    # print '<clocks.py not inside local test> DB_port: ', DB_port

  
except:
	print 'clocks data base credentials failed to gather'


	# Make current data table if it doesn't exist
try:
    print 'got in'
    conn = psycopg2.connect(database=DB_name,user=DB_user,password=DB_password,host=DB_host,port=DB_port,sslmode='require')
    print 'made connection'
    cur = conn.cursor()
    
    print 'test inside try make table'

    cur.execute("CREATE TABLE Current_Data(Date_time VARCHAR(35),\
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
    conn.close()
    print 'made table'
except:
    print 'clocks.py failed to connect or the table was already created'









@sched.scheduled_job('cron', day_of_week='mon-fri', hour='6-22', minute='*/3')
def scheduled_job_1():
    print('This job is run every weekday every 3 minutes with the hour addition.')
    tz = timezone('EST')
    date_time=datetime.now(tz).isoformat()
    print 'Date time: ' + date_time    




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


