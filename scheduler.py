
from redis import Redis
from rq_scheduler import Scheduler
from worker import archive_expired_items

redis_conn = Redis()
scheduler = Scheduler(connection=redis_conn)

scheduler.cron(
    "0 0 * * *",   # every day at 00:00
    # "* * * * *",  # every minute for testing now
    # "*/5 * * * *", #every 5 minute for testing better
    func=archive_expired_items,
    repeat=None
)