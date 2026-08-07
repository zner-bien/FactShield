import re


class TextCleaner:

    @staticmethod
    def clean(text: str) -> str:

        if not text:
            return ""

        # Remove URLs
        text = re.sub(r"http\S+", "", text)

        # Remove HTML
        text = re.sub(r"<.*?>", "", text)

        # Remove extra spaces
        text = re.sub(r"\s+", " ", text)

        return text.strip()