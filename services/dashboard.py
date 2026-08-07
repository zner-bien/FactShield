from services.history import HistoryManager


class DashboardAnalytics:

    @staticmethod
    def generate():

        history = HistoryManager.load()

        total = len(history)

        real = sum(
            1 for item in history
            if item["prediction"] == "REAL"
        )

        fake = sum(
            1 for item in history
            if item["prediction"] == "FAKE"
        )

        average_confidence = 0
        average_credibility = 0
        average_clickbait = 0
        average_bias = 0

        if total > 0:

            average_confidence = sum(
                item["confidence"]
                for item in history
            ) / total

            average_credibility = sum(
                item["credibility"]
                for item in history
            ) / total

            average_clickbait = sum(
                item["clickbait"]
                for item in history
            ) / total

            average_bias = sum(
                item["bias"]
                for item in history
            ) / total

        return {

            "total": total,

            "real": real,

            "fake": fake,

            "avg_confidence": round(
                average_confidence,
                2
            ),

            "avg_credibility": round(
                average_credibility,
                2
            ),

            "avg_clickbait": round(
                average_clickbait,
                2
            ),

            "avg_bias": round(
                average_bias,
                2
            ),

            "history": history[:10]

        }