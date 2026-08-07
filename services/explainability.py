import os
import joblib
import numpy as np


class Explainability:

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

    def explain(self, article, top_n=10):

        article_vector = self.vectorizer.transform(
            [article]
        )

        feature_names = np.array(
            self.vectorizer.get_feature_names_out()
        )

        coefficients = self.model.coef_[0]

        indices = article_vector.nonzero()[1]

        words = feature_names[indices]

        weights = coefficients[indices]

        ranked = sorted(

            zip(words, weights),

            key=lambda x: abs(x[1]),

            reverse=True

        )

        real_words = [

            word

            for word, weight in ranked

            if weight > 0

        ][:top_n]

        fake_words = [

            word

            for word, weight in ranked

            if weight < 0

        ][:top_n]

        return {

            "real": real_words,

            "fake": fake_words

        }