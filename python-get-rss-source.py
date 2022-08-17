import pprint
from rss_helper import RSSHelper

rss_feed = 'https://finance.yahoo.com/news/rssindex'

rsh = RSSHelper()
sources = rsh.get_rss_source(rss_feed)
pprint.pprint(sources)
