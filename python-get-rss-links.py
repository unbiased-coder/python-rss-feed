import pprint
from rss_helper import RSSHelper

rss_feed = 'https://finance.yahoo.com/news/rssindex'

rsh = RSSHelper()
links = rsh.get_rss_links(rss_feed)
pprint.pprint(links)
