import re


class BiasDetector:

    LOADED_WORDS = [

        "corrupt",
        "corruption",
        "lies",
        "lying",
        "propaganda",
        "evil",
        "disastrous",
        "catastrophic",
        "terrible",
        "outrageous",
        "shocking",
        "horrific",
        "criminal",
        "fraud",
        "scandal",
        "destroy",
        "attack",
        "extremist",
        "radical",
        "manipulation",
        "cover-up",
        "fake",
        "hoax",
        "agenda",
        "biased",
        "illegal",
        "dangerous",
        "panic",
        "crisis"

    ]


    @staticmethod
    def analyze(text):

        if not text:

            return {

                "score": 0,

                "level": "Low",

                "matches": []

            }

        sample = text.lower()

        matches = []

        score = 0

        for word in BiasDetector.LOADED_WORDS:

            occurrences = len(
                re.findall(r"\b" + re.escape(word) + r"\b", sample)
            )

            if occurrences:

                matches.append(word)

                score += occurrences * 5

        score = min(score, 100)

        if score >= 70:

            level = "High"

        elif score >= 35:

            level = "Moderate"

        else:

            level = "Low"

        return {

            "score": score,

            "level": level,

            "matches": matches

        }