import feedparser

FEEDS = [
    "https://azure.microsoft.com/en-us/updates/feed/",
    "https://devblogs.microsoft.com/feed/",
    "https://github.blog/feed/"
]

def fetch_news():
    articles = []

    for url in FEEDS:
        feed = feedparser.parse(url)

        for entry in feed.entries[:5]:
            articles.append({
                "title": entry.title,
                "summary": entry.summary,
                "link": entry.link
            })

    return articles[:5]