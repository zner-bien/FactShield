import json
import os
from datetime import datetime


class HistoryManager:

    FILE_PATH = "data/analysis_history.json"

    @classmethod
    def load(cls):

        if not os.path.exists(cls.FILE_PATH):

            return []

        with open(cls.FILE_PATH, "r", encoding="utf-8") as file:

            try:

                return json.load(file)

            except json.JSONDecodeError:

                return []

    @classmethod
    def save(cls, record):

        history = cls.load()

        history.insert(0, record)

        with open(cls.FILE_PATH, "w", encoding="utf-8") as file:

            json.dump(history, file, indent=4)

    @classmethod
    def create_record(
        cls,
        prediction,
        confidence,
        credibility,
        publisher,
        clickbait,
        bias
    ):

        return {

            "date": datetime.now().strftime(
                "%Y-%m-%d %H:%M"
            ),

            "prediction": prediction,

            "confidence": round(confidence, 2),

            "credibility": round(credibility, 2),

            "publisher": publisher,

            "clickbait": clickbait["score"],

            "bias": bias["score"]

        }