import asyncio
import requests
from utility import URLS, print_response
import time


@asyncio.coroutine
def get_response():
    loop = asyncio.get_event_loop()
    futures = []
    for u in URLS:
        f = loop.run_in_executor(None, requests.get, u)
        futures.append(f)

    for f in futures:
        r = yield from f
        print_response(r.text)


loop = asyncio.get_event_loop()
start_time = time.time()
loop.run_until_complete(get_response())
print(time.time() - start_time)
