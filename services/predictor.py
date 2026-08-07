import os
import joblib
import numpy as np


class FakeNewsPredictor:

    def __init__(self):

        # ==========================================
        # PROJECT ROOT DIRECTORY
        # ==========================================

        base_dir = os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )

        # ==========================================
        # MODEL PATHS
        # ==========================================

        model_path = os.path.join(
            base_dir,
            "trained_models",
            "factshield_model.pkl"
        )

        vectorizer_path = os.path.join(
            base_dir,
            "trained_models",
            "tfidf_vectorizer.pkl"
        )

        # ==========================================
        # LOAD MODEL
        # ==========================================

        self.model = joblib.load(
            model_path
        )

        self.vectorizer = joblib.load(
            vectorizer_path
        )

    # ==========================================
    # PREDICT ARTICLE
    # ==========================================

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

        # ==========================================
        # CONFIDENCE SCORE
        # ==========================================

        if hasattr(
            self.model,
            "predict_proba"
        ):

            probability = self.model.predict_proba(
                article_vector
            )[0]

            confidence = round(
                float(np.max(probability)) * 100,
                2
            )

        elif hasattr(
            self.model,
            "decision_function"
        ):

            score = self.model.decision_function(
                article_vector
            )[0]

            confidence = round(
                100 / (1 + np.exp(-abs(score))),
                2
            )

        else:

            confidence = 95.00

        # ==========================================
        # RETURN RESULT
        # ==========================================

        return {

            "prediction": label,

            "confidence": confidence

        }