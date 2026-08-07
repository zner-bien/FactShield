from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


class ArticleSummarizer:

    @staticmethod
    def summarize(text, sentences=3):

        try:

            if not text or len(text.strip()) < 100:

                return "The submitted article is too short to generate a meaningful summary."

            parser = PlaintextParser.from_string(
                text,
                Tokenizer("english")
            )

            summarizer = LsaSummarizer()

            summary = summarizer(
                parser.document,
                sentences
            )

            summary_text = " ".join(
                str(sentence)
                for sentence in summary
            )

            return summary_text

        except Exception:

            return "Summary could not be generated."