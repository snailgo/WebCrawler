import urlparse
from LinkFinder import LinkFinder
import urllib
from general import *

__author__ = 'Pengfei Wu'

MAX_CRAWLED_PAGE_NUM = 10
WORK_DIR = 'build'

class WebCrawler:
    base_url = ''
    project_name = ''
    queue = dict()
    crawled = dict()
    queue_file = 'queue.csv'
    crawled_file = 'crawled.csv'

    def __init__(self, project_name, base_url):
        # Basic info
        WebCrawler.base_url = base_url
        WebCrawler.project_name = project_name
        # Setup directory and file
        WebCrawler.queue_file = os.path.join(WORK_DIR, os.path.join(project_name, WebCrawler.queue_file))
        WebCrawler.crawled_file = os.path.join(WORK_DIR, os.path.join(project_name, WebCrawler.crawled_file))
        createWorkDir(os.path.join(WORK_DIR, WebCrawler.project_name))
        # Init queue 
        WebCrawler.queue = readFile(WebCrawler.queue_file)
        WebCrawler.crawled = readFile(WebCrawler.crawled_file)
        WebCrawler.queue[WebCrawler.base_url] = (WebCrawler.project_name, 'This is start point')


    # Maintain queue and crawled dict
    # get result from crawl_page and merge it to queue
    # input resource: queue, crawled
    # while queue not empty:
    #       crawl one page
    #       update queue and crawl
    #       update queue and crawl file
    # end
    @staticmethod
    def run():
        while len(WebCrawler.crawled) < MAX_CRAWLED_PAGE_NUM and len(WebCrawler.queue) > 0:
            (target_url, target_value) = WebCrawler.queue.popitem()
            found_links = WebCrawler.crawl_page(target_url)
            for n_url, n_value in found_links.iteritems():
                if n_url in WebCrawler.queue:
                    continue
                if n_url in WebCrawler.crawled:
                    continue
                WebCrawler.queue[n_url] = n_value
            WebCrawler.crawled[target_url] = target_value
            # write to file 
            appendFile(WebCrawler.crawled_file, target_url, target_value) 
        writeFile(WebCrawler.queue_file, WebCrawler.queue)

    # Crawled one page and return result
    # input: target_url
    # output: dictionary of link and data
    # requirement: link are completed 
    @staticmethod
    def crawl_page(target_url):
        page_string = urllib.urlopen(target_url).read()
        link_finder = LinkFinder()
        link_finder.feed(page_string)
        raw_links = link_finder.get_found_links()
        completed_links = {}
        for k, v in raw_links.iteritems():
            comp_link = urlparse.urljoin(WebCrawler.base_url, k)
            if comp_link.lower().endswith('.html'):
                completed_links[comp_link] = v
        return completed_links


