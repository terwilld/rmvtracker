from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()



# @sched.scheduled_job('interval', minutes=3)
# def timed_job():
#     print('This job is run every three minutes.')
print 'test_1_!_1'
@sched.scheduled_job('cron', day_of_week='mon-fri',minute='*/3')
def scheduled_job():
    print('This job is run every weekday every 3 minutes.')


print 'test_2_@_2_2_@'

sched.start()