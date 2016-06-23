"""
    This model implements a LinkFinder which mainly has
two functions:
    1. get a web page
    2. parse web page and create records
"""
from HTMLParser import HTMLParser
import pprint

class LinkFinder(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.found_links = {}
        self.curr_link = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.curr_link = [value for (key, value) in attrs if key == 'href']
            if len(self.curr_link) == 1:
                self.curr_link = self.curr_link[0]

    def handle_endtag(self, tag):
        if tag == 'a':
            self.curr_link = ''

    def handle_data(self, data):
        if len(self.curr_link) > 0:
            self.found_links[self.curr_link] = data

    def print_links(self):
        pprint.pprint(self.found_links) 

    
    def get_found_links(self):
        return self.found_links

# simple test
linkFinder = LinkFinder()
linkFinder.feed("<html><a href='www.google.com'>Google</a></html>")
linkFinder.print_links()
