from urllib.parse import urlparse


class SourceReputation:

    TRUSTED = {
        "reuters.com",
        "apnews.com",
        "bbc.com",
        "bbc.co.uk",
        "cnn.com",
        "nytimes.com",
        "washingtonpost.com",
        "theguardian.com",
        "npr.org",
        "forbes.com",
        "bloomberg.com",
        "abcnews.go.com",
        "cbsnews.com",
        "nbcnews.com",
        "time.com",
        "usatoday.com"
    }

    GENERALLY_RELIABLE = {
        "news.yahoo.com",
        "msn.com",
        "cnet.com",
        "foxnews.com",
        "aljazeera.com"
    }

    @staticmethod
    def analyze(url):

        if not url:

            return {
                "domain": "N/A",
                "rating": "Not Available",
                "stars": 0,
                "color": "gray"
            }

        domain = urlparse(url).netloc.lower()

        domain = domain.replace("www.", "")

        if domain in SourceReputation.TRUSTED:

            return {
                "domain": domain,
                "rating": "Trusted News Source",
                "stars": 5,
                "color": "green"
            }

        if domain in SourceReputation.GENERALLY_RELIABLE:

            return {
                "domain": domain,
                "rating": "Generally Reliable",
                "stars": 4,
                "color": "yellow"
            }

        return {
            "domain": domain,
            "rating": "Unknown / Unverified",
            "stars": 2,
            "color": "red"
        }