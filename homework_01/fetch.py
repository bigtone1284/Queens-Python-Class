#
# Assignment: Write a function to parse URLs.
# 
# Fill in the body of the 'urlparse()' function in this module.  If you wish,
# you may define and use additional helper functions; these generally will make
# your code clearer.
#
# To test your solution, use the unit test script provided along with this file.
# The unit test script will import your version of this module, and test your
# solution by running it with specific inputs and checking the answers.  It will
# tell you if all the tests produce the expected results or not.
#

from collections import namedtuple
from urllib import request

ParseResult = namedtuple('ParseResult', 'scheme, netloc, path, params, query, fragment')


def urlparse(url):
    scheme = netloc = path = params = query = fragment = ''
    
    if "#" in url and "?" in url:
    	query =url[url.index("?")+1:url.index("#")]
    	fragment =url[url.index("#")+1:]
    else:
    	if "#" in url:
    		fragment =url[url.index("#")+1:]
    	elif "?" in url:
    		query =url[url.index("?")+1:]
    
    if "://" in url:
    	scheme = (url[0:url.index("://")]).lower()
    	if "/" not in url[(url.index("://")+3):]:
    		netloc = url[url.index("://")+3:]
    else:
    	if "/" not in url:
    		path = url
    	else:
    		if "/" not in url[url.index("//")+2:]:
    			netloc = url[url.index("//")+2:]
    		else:
    			netloc = url[url.index("//")+2: (url[url.index("//")+3:].index("/")) + 3  ]
    			if "?" not in url and "#" not in url:
    				path = url[(url[url.index("//")+3:].index("/")) + 3:]
    			
    			elif "?" in url:
    				path = url[(url[url.index("//")+3:].index("/")) + 3: url.index("?")]
    			
    			elif "#" in url and "?" not in url:
    				path = url[(url[url.index("//")+3:].index("/")) + 3: url.index("#")]	
    			
    			
    				
    			
    
    
	
    

    return (ParseResult(scheme, netloc, path, params, query, fragment))
    
#q = '//example.com:8042/over/there?name=ferret'
#urlparse(q)
