from urllib.parse import urlparse


class MetadataExtractor:

    @staticmethod
    def publisher(url):

        domain = urlparse(url).netloc

        domain = domain.replace("www.", "")

        publisher = domain.split(".")[0]

        return publisher.title()

    @staticmethod
    def publication_date(date):

        if date is None:
            return "Unknown"

        return date.strftime("%B %d, %Y")