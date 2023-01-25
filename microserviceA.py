import time, requests

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
name = 'microserviceA'

try:
    redis_conn.xgroup_create(key, group)
except:
    print('Group already exists!')


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    # print(request.method, request.url, request.url.port, request.url.scheme, request.url.path, sep='\n')
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    if request.url.path == '/process':
        redis_conn.xadd(key, {"name": name, "process-time": process_time}, '*')
        # print(name, process_time)
    return response

@app.get('/process')
async def process(id: str, value: int):
    req = requests.get(f'http://localhost:3002/products/?id={id}&value={value*2}')
    return {"action":"success"}

@app.get('/settings')
async def process(setting: str, value: int):
    return {"action":"success"}