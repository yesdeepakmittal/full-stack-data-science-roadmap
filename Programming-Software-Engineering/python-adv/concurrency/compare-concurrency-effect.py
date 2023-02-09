# https://www.youtube.com/watch?v=GpqAQxH1Afc
import asyncio

import requests
from time import perf_counter

RQST_CNT = 100

def get_joke():
    res = requests.get('https://official-joke-api.appspot.com/random_joke')
    return res.json().get('setup')

async def my_async_call():
    return await asyncio.to_thread(get_joke)

def my_sync_call():
    return get_joke()
    
async def main_function():
    
    # synchronous     
    time_start = perf_counter()
    
    for i in range(RQST_CNT):
        my_sync_call()
    print(f"Time taken in Synchronous Call: {perf_counter() - time_start}")
    
    # asynchronous     
    time_start = perf_counter()
    
    # for i in range(RQST_CNT):
    #     await my_async_call()
    await asyncio.gather(*[my_async_call() for i in range(RQST_CNT)])
    print(f"Time taken in Asynchronous Call: {perf_counter() - time_start}")
    
asyncio.run(main_function())