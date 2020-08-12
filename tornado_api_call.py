from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop
from utility import URLS
import json
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
        parsed_body = json.loads(response.body)
        for m in parsed_body:
            try:
                print(
                    m['match_date'] + ': ' + m['match_hometeam_name'] + ':' + m['match_awayteam_name'] + ' ----> ' +
                    m['match_hometeam_score'] + ':' + m['match_awayteam_score'])
            except TypeError:
                pass
        count += 1
        if count == len(URLS):
            loop.stop()

for u in URLS:
    loop.add_callback(send_request, u)

start_time = time.time()
loop.start()
print(time.time() - start_time)


