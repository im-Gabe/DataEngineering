import urllib.request
import json
import datetime as dt
import pytz
timezone = pytz.timezone("US/Pacific")
date = dt.datetime.today()
today = timezone.localize(date)
#today = date.today().replace(timezone(-8))
data = urllib.request.urlopen("http://rbi.ddns.net/getBreadCrumbData")
name = "BreadCrumbData{today}.json".format(today = today)
name = name[:24]+".json"
raw = data.read()
f = open(name, 'wb')
f.write(raw)
f.close()
