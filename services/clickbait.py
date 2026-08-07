import re


class ClickbaitDetector:

    TRIGGERS = [

        "you won't believe",
        "shocking",
        "what happened next",
        "this is why",
        "secret",
        "revealed",
        "unbelievable",
        "must see",
        "everyone is talking",
        "breaking",
        "exclusive",
        "viral",
        "mind blown",
        "amazing",
        "incredible",
        "can't believe",
        "watch",
        "warning",
        "urgent"

    ]

    @staticmethod
    def analyze(text):

        if not text:

            return {
                "score": 0,
                "risk": "Low",
                "matches": []
            }

        sample = text[:500].lower()

        matches = []

        score = 0

        for phrase in ClickbaitDetector.TRIGGERS:

            if phrase in sample:

                matches.append(phrase)

                score += 10

        exclamations = sample.count("!")

        score += min(exclamations * 3, 15)

        capitals = len(re.findall(r"\b[A-Z]{4,}\b", text))

        score += min(capitals * 5, 15)

        score = min(score, 100)

        if score >= 70:

            risk = "High"

        elif score >= 40:

            risk = "Moderate"

        else:

            risk = "Low"

        return {

            "score": score,

            "risk": risk,

            "matches": matches

        }