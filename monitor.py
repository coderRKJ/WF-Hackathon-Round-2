from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from redis_om import get_redis_connection

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

redis_conn = get_redis_connection()

key = 'time'
group = 'monitor'
names = ['microserviceB','microserviceB','microserviceB']

try:
    redis_conn.xgroup_create(key, group)
except:
    print('Group already exists!')

@app.get('/metrics')
async def metrics():
    results = redis_conn.xreadgroup(group, key, {key: '>'}, None)
    return results

@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})