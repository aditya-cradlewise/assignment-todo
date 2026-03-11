from redis import Redis
from rq import Queue
from app.repository.todo_repository import TodoRepository


redis_conn = Redis()
queue = Queue(connection=redis_conn)

def archive_expired_items():
    print("Running archive job...")
    repo = TodoRepository()
    repo.archive_expired_items()
