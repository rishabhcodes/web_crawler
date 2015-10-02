'''
Created on Sep 27, 2015

@author: risshah
'''
# temporarily using page directly. Will later be passed as parameter to this function

page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://www.xkcd.com">')

# pattern to be isolated

pattern = '<a href='

# increment is used move the pointer in string appropriately
increment = 1

# initialized url
url = ''
 
# starting position of url  
start_link = (page.find(pattern)) + len(pattern) + increment

# ending position of url
end_link = page.find('"',start_link)

# isolated url just being printed for now
print page[start_link:end_link]