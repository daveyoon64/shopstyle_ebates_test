import hmac
import hashlib
import json
import requests
import time
import datetime

# original URL
# http://api.viki.io/v4/videos.json?app=100250a&per_page=10&page=1

base_url = 'http://api.viki.io/v4/movies.json?sort=views'
app_id = '&app=100660a'
time = int(time.time())
time_stamp = '&t=' + str(time)
page_setup = '&per_page=10&page=1'

url = base_url + app_id + time_stamp
url = url.encode('utf-8')
secret = <ENTER SECRET>
dig = hmac.new(secret, url, hashlib.sha1)
dig.update(url)
sig = dig.hexdigest()

complete_url = base_url + app_id
headers = {'timestamp': time_stamp, 'signature': sig}
r = requests.get(complete_url, headers=headers)
print(r.text)
