from config import URL, date_from, date_to, APIkey, league_id
import datetime


URLS = []
start_date = datetime.datetime.strptime(date_from, "%Y-%m-%d")
end_date = datetime.datetime.strptime(date_to, "%Y-%m-%d")

while end_date.month <= 12:
    url = URL + '&from=' + start_date.strftime("%Y-%m-%d") + '&to=' + end_date.strftime("%Y-%m-%d") \
          + '&league_id=' + league_id + '&APIkey=' + APIkey
    URLS.append(url)
    start_date = datetime.date(start_date.year, end_date.month, 1)
    if end_date.month + 1 == 13:
        break
    end_date = datetime.date(start_date.year, end_date.month + 1, 1)

