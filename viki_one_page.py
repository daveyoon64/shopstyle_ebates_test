import requests
import json

true_flags = 0
false_flags = 0
headers = {
   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

# create url for next page
url = 'http://api.viki.io/v4/videos.json?app=100250a&per_page=10&page=%d'
page_counter = 1
next_url = url % page_counter

# get the response and convert to json
r = requests.get((next_url), headers=headers)
r_json = r.json()

# parse for 'hd'
def tally_hd_flags(my_dict):
    global true_flags, false_flags
    for key, value in r_json.items():
        if isinstance(value, list):
            for d in value:
                if (d['flags']['hd'] == True):
                    true_flags += 1
                elif (d['flags']['hd'] == False):
                    false_flags += 1
                else:
                    continue
# final output
tally_hd_flags(r_json)
print("Total true flags: ", true_flags)
print("Total false flags: ", false_flags)
