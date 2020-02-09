from apscheduler.schedulers.blocking import BlockingScheduler
import driver

sched = BlockingScheduler()

#13:30 in usa(heroku server) == 00:00 in India
@sched.scheduled_job('cron', hour=13, minute=30)
def notify():
    driver.execute()


sched.start()


def terminate():
    sched.shutdown()
