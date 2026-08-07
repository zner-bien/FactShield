import os
import joblib
import numpy as np


class FakeNewsPredictor:

    def __init__(self):

        model_path = os.path.join(
            "trained_models",
            "factshield_model.pkl"
        )

        vectorizer_path = os.path.join(
            "trained_models",
            "tfidf_vectorizer.pkl"
        )

        self.model = joblib.load(model_path)

        self.vectorizer = joblib.load(vectorizer_path)

    def predict(self, article):

        article_vector = self.vectorizer.transform(
            [article]
        )

        prediction = self.model.predict(
            article_vector
        )[0]

        label = "REAL"

        if prediction == 0:
            label = "FAKE"

        confidence = None

        # Models with probability support
        if hasattr(self.model, "predict_proba"):

            probability = self.model.predict_proba(
                article_vector
            )[0]

            confidence = round(
                float(np.max(probability)) * 100,
                2
            )

        # LinearSVC (uses decision function)
        elif hasattr(self.model, "decision_function"):

            score = self.model.decision_function(
                article_vector
            )[0]

            confidence = round(
                100 / (1 + np.exp(-abs(score))),
                2
            )

        else:

            confidence = 95.00

        return {

            "prediction": label,

            "confidence": confidence

        }