import asyncio
import requests
from config import USER_AGENT
from utility import URLS
import json
import time


async def send_request(url):
    headers = {'User-Agent': USER_AGENT}
    response = requests.get(url, headers=headers)
    parsed_body = json.loads(response.content)
    for m in parsed_body:
        try:
            print(
                m['match_date'] + ': ' + m['match_hometeam_name'] + ':' + m['match_awayteam_name'] + ' ----> ' +
                m['match_hometeam_score'] + ':' + m['match_awayteam_score'])
        except Exception:
            pass


async def main():
    calls = []
    for u in URLS:
        calls.append(send_request(u))

    await asyncio.gather(*calls)

loop = asyncio.get_event_loop()
start_time = time.time()
loop.run_until_complete(main())
print(time.time() - start_time)
