import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)

redis_conn = get_redis_connection()

key = 'time'
group = 'monitor'
name = 'microserviceC'

try:
    redis_conn.xgroup_create(key, group)
except:
    print('Group already exists!')


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    redis_conn.xadd(key, {"name": name, "process-time": process_time}, '*')
    return response

@app.get('/process')
async def process(id: str, value: int):
    return {"action":"success"}