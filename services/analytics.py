import json
import os


class DashboardAnalytics:

    HISTORY_FILE = "data/analysis_history.json"

    @staticmethod
    def generate():

        if not os.path.exists(DashboardAnalytics.HISTORY_FILE):

            return {

                "total": 0,

                "real": 0,

                "fake": 0,

                "avg_confidence": 0,

                "avg_credibility": 0,

                "avg_clickbait": 0,

                "avg_bias": 0

            }

        with open(

            DashboardAnalytics.HISTORY_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            history = json.load(file)

        if len(history) == 0:

            return {

                "total": 0,

                "real": 0,

                "fake": 0,

                "avg_confidence": 0,

                "avg_credibility": 0,

                "avg_clickbait": 0,

                "avg_bias": 0

            }

        real_count = sum(
            1 for item in history
            if item["prediction"] == "REAL"
        )

        fake_count = sum(
            1 for item in history
            if item["prediction"] == "FAKE"
        )

        avg_confidence = round(

            sum(item["confidence"] for item in history)

            / len(history),

            2

        )

        avg_credibility = round(

            sum(item["credibility"] for item in history)

            / len(history),

            2

        )

        avg_clickbait = round(

            sum(item["clickbait"] for item in history)

            / len(history),

            2

        )

        avg_bias = round(

            sum(item["bias"] for item in history)

            / len(history),

            2

        )

        return {

            "total": len(history),

            "real": real_count,

            "fake": fake_count,

            "avg_confidence": avg_confidence,

            "avg_credibility": avg_credibility,

            "avg_clickbait": avg_clickbait,

            "avg_bias": avg_bias

        }