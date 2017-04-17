# ShopStyle at Ebates Take Home
 * This script will call the Viki API v4 endpoint
 * It will parse the repsonse as a JSON
 * It will then look for a 'flags' key, and then check for a 'hd' key.
 * It will then continually increment the pages until the 'more' key returns false.
 * Finally, he script will then print out how many response objects are true and how many are false.

# Process
## Initial Commit
 * I read the API docs and try making requests with their SHA1-HMAC signature.
 * I break the problem down and get the first page meeting the criteria.

## Second Pass

# Environment
I used virtualenv & virtualenvwrapper with pip managing my custom packages.
Sublime was my primary text editor with the Python 3.6 interpreter (via Mac Terminal). 

# Modules used
 * Scrapy 1.2.1
 * Twisted 16.4.1 (currently there is a bug with Scrapy and Twisted 17.1)
 * Requests (2.13.0)
