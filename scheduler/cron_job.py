from datetime import datetime
from pytz import timezone
import driver
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

tz = datetime.now(timezone('UTC')).astimezone(timezone('Asia/Kolkata'))


@sched.scheduled_job('cron', hour=23, minute=59, second=30, timezone=tz)
def notify():
    driver.execute()


sched.start()


def terminate():
    sched.shutdown()
