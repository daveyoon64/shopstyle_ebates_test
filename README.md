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
 * I keep it simple when planning the crawling. I intially try out a simple recursion.
 * Although this works, there's a lot of concerns in terms of memory usage and Python's limited recursion capabilities.
 * The test takes awhile (roughly > 10 minutes) and the stack frame uses quite a bit of memory!
 * I have a working solution and now I try to make it more readable and reusable.

## Third Pass
 * I start to look for better solutions and modules!
 * I come across the Scrapy module, which works well with the yield generator to check all the required pages.
 * Rewrote as the class VikiSpider() to make it reusuable.
 * The modification is much faster! (around 4 minutes) uses much less memory.

## Final Notes
 * In all my tests, I always got 10,000 'hd': 'true' and 0 'hd': 'false'. I'm suspicious that my tests were "perfect" and wanted to test this further, given more time.
 * I may have violated Internet etiquette by scraping api.viki.io a bit aggressively. I would probably spend a time implementing Scrapy's AutoThrottle extension to fine tune an optimal crawling speed.

# Environment
I used virtualenv & virtualenvwrapper with pip managing my custom packages.
Sublime was my primary text editor with the Python 3.6 interpreter (via Mac Terminal). 

# Modules used
 * Scrapy 1.2.1
 * Twisted 16.4.1 (currently there is a bug with Scrapy and Twisted 17.1)
 * Requests (2.13.0)
