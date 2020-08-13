import asyncio
import requests
from utility import URLS
import json
import time


def print_response(body):
    parsed_body = json.loads(body)
    for m in parsed_body:
        try:
            print(
                m['match_date'] + ': ' + m['match_hometeam_name'] + ':' + m['match_awayteam_name'] + ' ----> ' +
                m['match_hometeam_score'] + ':' + m['match_awayteam_score'])
        except Exception:
            pass


@asyncio.coroutine
def main():
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
loop.run_until_complete(main())
print(time.time() - start_time)
