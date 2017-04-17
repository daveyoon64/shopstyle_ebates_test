import requests
import json
import sys

true_flags = 0
false_flags = 0
headers = {
   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

# create url for next page
url = 'http://api.viki.io/v4/videos.json?app=100250a&per_page=10&page=%d'
page_number = 1

sys.setrecursionlimit(1500)

def tally_hd_flags(next_url):
    global true_flags, false_flags, headers, url, page_number
    
    print(page_number)

    r = requests.get((next_url), headers=headers)
    r_json = r.json()
    for key, value in r_json.items():
        if isinstance(value, list):
            for d in value:
                if (d['flags']['hd'] == True):
                    true_flags += 1
                elif (d['flags']['hd'] == False):
                    false_flags += 1
                else:
                    continue

    if r_json['more'] == True:
        page_number += 1
        tally_hd_flags(url % page_number)

# final output
#tally_hd_flags(r_json)
tally_hd_flags(url % 1)

print("Total true flags: ", true_flags)
print("Total false flags: ", false_flags)