from newspaper import Article


class NewsScraper:

    @staticmethod
    def scrape(url):

        article = Article(url)

        article.download()

        article.parse()

        return {
            "title": article.title,
            "text": article.text,
            "authors": article.authors,
            "publish_date": article.publish_date
        }