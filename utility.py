from config import URL, year, APIkey, league_id
import datetime
from calendar import monthrange
import json

URLS = []

for month in range(1, 13):
    start_date = datetime.datetime(year, month, 1)
    end_date = datetime.datetime(year, month, monthrange(2019, month)[1])
    url = URL + '&from=' + start_date.strftime("%Y-%m-%d") + '&to=' + end_date.strftime("%Y-%m-%d") \
          + '&league_id=' + league_id + '&APIkey=' + APIkey
    URLS.append(url)


def print_response(body):
    parsed_body = json.loads(body)
    for m in parsed_body:
        try:
            print(
                m['match_date'] + ': ' + m['match_hometeam_name'] + ':' + m['match_awayteam_name'] + ' ----> ' +
                m['match_hometeam_score'] + ':' + m['match_awayteam_score'])
        except Exception:
            pass
