from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()



# @sched.scheduled_job('interval', minutes=3)
# def timed_job():
#     print('This job is run every three minutes.')

@sched.scheduled_job('cron', day_of_week='mon-fri', hour='6-22', minute='*/3')
def scheduled_job_1():
    print('This job is run every weekday every 3 minutes with the hour addition.')


print 'test_1_!_1'
@sched.scheduled_job('cron', day_of_week='mon-fri', minute='*/3')
def scheduled_job():
    print('This job is run every weekday every 3 minutes without the hour addition.')
    print '123432123'



print 'test_2_@_2_2_@'

sched.start()


