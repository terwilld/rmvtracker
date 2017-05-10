import psycopg2
import os.path,urllib2,requests,datetime,csv,time,logging
from bs4 import BeautifulSoup
import datetime
import pytz



def get_current_wait_times(town_name):
    '''takes town_name which is a string {first letter cap} completes its URL, scrapes the two times [licensing and registration] returns them as two length list containing strings'''
        #   Makes the complete URL, Martha's Vinyard is handled differently by the template
    if town_name=='Martha%27s%20Vineyard':
        url = 'http://www.massrmv.com/index/tabid/3353/ctl/accessible/mid/9589/Default.aspx?Name=Martha%27s%20Vineyard'
    else:
        url = 'http://www.massrmv.com/index/tabid/3353/ctl/accessible/mid/9589/Name/'+str(town_name)+'/Default.aspx'

        #   Creates soup of URL to search for specifi class
    try:
        r  = requests.get(url)
    except Exception, e:
        #errors fill the array with -30s for debugging
        f = open('log.txt', 'w')
        f.write('Failure with requests.get(URL)'+url+' - %s' % e)
        f.close()
        print 'Houston we have a problem.  Most likely a timed out request', url
        return [-30,-30]
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    
        #   Results are stored as two specific classes within the HTML.  Each are retrieved and stored as a string
    results=[]    
        #   Licensing stored first
    spans = soup.find_all('span', attrs={'id':'dnn_ctr9589_ViewBranchAccessible_lblLicensing'})
    for span in spans:
        #   Try is used incase type conversion fails -30 is stored as a value to indicate a failure
        try:
            results+=[str(span.string)]
        except Exception, e:
            print 'error with town licensing: ',town_name,' Troublesome string is: ', span.string
            f = open('log.txt', 'w')
            f.write('Trouble handling string from ID'+url+' - %s' % e)
            f.close()
            results+=[-30]
            #   Should eventually print to a fail_log
        #   Registration stored second    
    spans = soup.find_all('span', attrs={'id':'dnn_ctr9589_ViewBranchAccessible_lblRegistration'})
    for span in spans:
        #   Try is used incase type conversion fails -30 is stored as a value to indicate a failure
        try:
            results+=[str(span.string)]
        except Exception, e:
            print 'error with town registration: ',town_name,' Troublesome string is: ', span.string
            f = open('log.txt', 'w')
            f.write('Trouble handling string from ID'+url+' - %s' % e)
            f.close()            
            results+=[-30]
    return results


 



def add_a_reading(list_of_towns):
    '''input date,time,list_of_towns. opens and writes results to current file makes file if it doesnt exist '''
    #   Results are 2x each town
    results=[]
    #   Results array filled with strings
    for town in list_of_towns:
        results+=get_current_wait_times(town)

    #   Convert results from strings to numbers exclude first two
    results=convert_results_to_minutes(results)

    #   Add results to CSV

    if len(results)==56:
        date_time=datetime.datetime.now(pytz.timezone("America/New_York")).isoformat()
        #print date_time
        results=[date_time]+results
        return results
    else:
        print results,'houston we have a problem dropped result'


def convert_results_to_minutes(results):
    '''input: list [first two entries are date,time then strings of wait times.  convert strings to numbers rounded to minute return same array'''

    #   Array has date and time, ignore first two.  
    for a in range(0,len(results)):
        #   Temporary holder for variable to check
        string_holder=results[a]
        #   Easiest possible outcome.  
        if string_holder=='No wait time':
            results[a]=0

        #   Closed should be graphed as -15 so that its obvious
        elif string_holder=='Closed':
            results[a]=-15

        #   If hours is in string its of format '1 hour, 13 minutes, 50 seconds'
        #   Return 60*hour plus minutes ignore seconds
        elif 'hour' in string_holder:
            try:
                number_of_hours=int(string_holder[:string_holder.index('hour')])
                string_holder=string_holder[(string_holder.index(',')+1):]
                number_of_minutes=int(string_holder[:string_holder.index('minute')])
                results[a]=number_of_hours*60+number_of_minutes
            except Exception, e:
                print 'string conversion error caused by', string_holder
                f = open('log.txt', 'w')
                f.write('string conversaion error caused by [hour in string]'+string_holder+' - %s' % e)
                f.close()            
                results[a]=-30

        #   If no hours in string return just the minutes ignore seconds.  Format: '14 minutes, 28 seconds'
        elif 'minute' in string_holder:
            try:
                results[a]=int(string_holder[:string_holder.index('minute')])
            except Exception, e:
                print 'string conversion error caused by', string_holder
                f = open('log.txt', 'w')
                f.write('string conversaion error caused by[minute in string but not hour] '+string_holder+' - %s' % e)
                f.close()            

        #   Just single digit seconds should count as zero rare, but crashed program a few times until logging detected.
        elif 'second' in string_holder:
            results[a]=0

        else:
            results[a]=-30
            print 'Houston we have a problem.  The string was not handled ', string_holder
            #this needs to be logged somehow
    return results
