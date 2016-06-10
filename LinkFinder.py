"""
    This model implements a LinkFinder which mainly has
two functions:
    1. get a web page
    2. parse web page and create records
"""

import urllib
from HTMLParser import HTMLParser

class LinkFinder(HTMLParser):
    self.target_url = ''

    def __init__(self, target_url):
        self.target_url = target_url 

    def handle_starttag(self, tag, attrs):
        pass

    def handle_endtag(self, tag, attrs):
        pass

    def handle_data(self, tag, attrs):
        pass
    
    def crawl_page():
        res = dict()
        page_
        
