'''
Created on Sep 27, 2015

@author: risshah
'''
# temporarily using page directly. Will later be passed as parameter to this function

#Utility function to get web page as a string
def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''
    
#Used as a utility function to extract one link at a time from the web page
def get_next_target(page):

    # pattern to be isolated
    pattern = '<a href='
    
    # increment is used move the pointer in string appropriately
    increment = 1
    
    if page.find(pattern) != -1:
    
        # starting position of url  
        start_link = (page.find(pattern)) + len(pattern) + increment
        
        # ending position of url
        end_link = page.find('"',start_link)
        
        # isolated url just being printed for now
        url = page[start_link:end_link]
        
        return(url, end_link)
    return(None, 0)

#Extracts all links from a web page 
def print_all_links(page):
    while True:
        url,end_link = get_next_target(page)
        if not url:
            break
        else:
            print url
            page = page[end_link:]
    return    

page = get_page('http://xkcd.com/353/')        
print_all_links(page)
        
        
        
        
        
        
        
        