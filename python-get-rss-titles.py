import pprint
from rss_helper import RSSHelper

rss_feed = 'https://finance.yahoo.com/news/rssindex'

rsh = RSSHelper()
titles = rsh.get_rss_titles(rss_feed)
pprint.pprint(titles)
