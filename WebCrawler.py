import urlparse
from general import *

__author__ = 'Pengfei Wu'

class WebCrawler:
    base_url = ''
    project_name = ''
    queue = dict()
    crawled = dict()
    queue_file = 'queue.csv'
    crawled_file = 'crawled.csv'

    def __init__(self, project_name, base_url):
        WebCrawler.base_url = base_url
        WebCrawler.project_name = project_name
        queue_file = os.path.join(project_name, queue_file)
        crawled_file = os.path.join(project_name, crawled_file) 
        createWorkDir(WebCrawler.project_name)
        queue = readFile(queue_file)
        crawled = readFile(crawled_file)
        queue[WebCrawler.base_url] = (WebCrawler.project_name, 'This is start point')

    @staticmethod
    def run():
        # parse page and write to file
