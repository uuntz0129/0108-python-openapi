from typing import Union
from fastapi import FastAPI
import redis
import os
from dotenv import load_dotenv
load_dotenv()
redis_conn = redis.Redis.from_url(os.environ.get('REDIS_HOST_PASSWORD'))

app = FastAPI()


@app.get("/")
def read_root():
    counter = redis_conn.incr('test:increment',1)
    return {"Counter": counter}

@app.get("/counter/{c}")
def counter(c:int):
    counter = redis_conn.incr('test:increment',c)
    return {"Counter": counter}


@app.get("/pico_w/{date}")
async def read_item(date:str ,address:str,celsius:float,light:float):
    print(f"日期:{date}")
    print(f"位置:{address}")
    print(f"攝氏:{celsius}")
    print(f"光線:{light}")
    return {"狀態":"儲存成功"}