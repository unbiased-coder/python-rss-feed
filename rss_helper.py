import feedparser

class RSSHelper:
    def __init__(self) -> None:
        return

    def get_rss_titles(self, rss_feed) -> list[str]:
        rss_feed = feedparser.parse(rss_feed)
        return [entry.title for entry in rss_feed.entries]

    def get_rss_links(self, rss_feed) -> list[str]:
        rss_feed = feedparser.parse(rss_feed)
        return [entry.link for entry in rss_feed.entries]

    def get_rss_source(self, rss_feed) -> list[dict]:
        rss_feed = feedparser.parse(rss_feed)
        return [entry.source for entry in rss_feed.entries]
