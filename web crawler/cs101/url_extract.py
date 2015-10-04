'''
Created on Sep 27, 2015

@author: risshah
'''
# temporarily using page directly. Will later be passed as parameter to this function

#Utility function to get web page as a string
def get_page(url):
    '''this function returns web page as a string
    given url as input'''
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''
    

def union(l1, l2):
    """takes 2 lists l1 and l2 as input and returns
    set union of the two"""
    
    for e in l2:
        if e not in l1:
            l1.append(e)
    return

def keyword_hash(keyword):
    """takes a string and returns a hash value"""
    hv = 0
    for c in keyword:
        hv = hv + ord(c)
    return hv
        
def hash_bucket(keyword,nbuckets):
    '''takes a keyword and total buckets & return the bucket specific to keyword'''
    hv = keyword_hash(keyword)
    bucket = hv%nbuckets
    return bucket

def create_index(nbuckets):
    '''creates and initializes the web index'''
    index = []
    i=0
    while i < nbuckets:
        index.append([])
        i=i+1
    return index

  
#Used as a utility function to extract one link at a time from the web page
def get_next_target(page):
    '''this function identifies the next url given the 
    web page as a string'''

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
def get_all_links(page):
    '''this function extracts all links from a web page'''
    url_list = []
    while True:
        url,end_link = get_next_target(page)
        if not url:
            break
        else:
            url_list.append(url)
            page = page[end_link:]
    return url_list   

def add_to_index(index,keyword,url,buckets):
    """This function takes a keyword & mutates the Index
    creating a mapping of the keyword to urls"""
    bucket = hash_bucket(keyword, buckets)
    for e in index[bucket]:
        if e[0] == keyword:
            e[1].append(url)
            return
    index[bucket].append([keyword,[url]])
    return

def add_page_to_index(index,page,url,buckets):
    '''adds the crawled web pages to the index'''
    for e in page.split():
        add_to_index(index,e,url,buckets)
    return

def crawler(seed):
    '''starts the crawl process provided a seed page'''
    to_crawl = [seed]
    crawled = []
    buckets = 4
    index = create_index(buckets)
    while to_crawl:
        url = to_crawl.pop()
        if url not in crawled:
            page = get_page(url)
            add_page_to_index(index, page, url, buckets)
            union(to_crawl,get_all_links(page))
            crawled.append(url)
        #need to figure out how to remove e from to_crawl
    return index 


print crawler('http://www.udacity.com/cs101x/index.html')        

        
        
        
        
        
        
        
        