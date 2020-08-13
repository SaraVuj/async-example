from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop
from utility import URLS, print_response
import time

count = 0
loop = IOLoop.current()


async def send_request(url):
    global count
    client = AsyncHTTPClient()

    try:
        response = await client.fetch(url)
    except Exception as e:
        print('Error' + str(e))
        count += 1
        if count == len(URLS):
            loop.stop()
    else:
        print_response(response.body)
        count += 1
        if count == len(URLS):
            loop.stop()

for u in URLS:
    loop.add_callback(send_request, u)

start_time = time.time()
loop.start()
print(time.time() - start_time)


