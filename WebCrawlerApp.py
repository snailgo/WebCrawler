#!/usr/bin/env python

from WebCrawler import WebCrawler

# initial crawler
# start crawler
# clean and exit
def mainloop():
    pass


# handle signal
# handle config
# go to main loop
def main():
    web_crawler = WebCrawler('Google', 'http://www.google.com')
    web_crawler.run()

if __name__ == '__main__':
    main()
