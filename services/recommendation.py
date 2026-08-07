class RecommendationGenerator:

    @staticmethod
    def generate(

        prediction,

        credibility,

        clickbait,

        bias,

        reputation

    ):

        recommendations = []

        if prediction == "FAKE":

            recommendations.append(
                "Avoid sharing this article until it has been verified."
            )

            recommendations.append(
                "Cross-check the information with trusted news organizations."
            )

        else:

            recommendations.append(
                "This article appears credible based on the AI analysis."
            )

            recommendations.append(
                "Continue verifying information from multiple reliable sources."
            )

        if credibility < 70:

            recommendations.append(
                "The credibility score is relatively low. Read with caution."
            )

        if clickbait["score"] >= 40:

            recommendations.append(
                "The headline contains clickbait characteristics."
            )

        if bias["score"] >= 40:

            recommendations.append(
                "The article contains emotionally loaded language."
            )

        if reputation:

            if reputation["stars"] <= 2:

                recommendations.append(
                    "The publisher has a relatively low reputation."
                )

        recommendations.append(
            "Always verify breaking news using official sources."
        )

        return recommendations