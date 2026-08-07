from flask import Flask, render_template, request

from services.cleaner import TextCleaner
from services.predictor import FakeNewsPredictor
from services.credibility import CredibilityAnalyzer
from services.scraper import NewsScraper
from services.extractor import MetadataExtractor
from services.summarizer import ArticleSummarizer
from services.reputation import SourceReputation
from services.file_handler import FileHandler
from services.clickbait import ClickbaitDetector
from services.bias import BiasDetector
from services.history import HistoryManager
from services.dashboard import DashboardAnalytics
from services.explainability import Explainability
from services.recommendation import RecommendationGenerator

app = Flask(__name__)

# ==========================================
# HOME
# ==========================================

@app.route("/")
def home():

    return render_template("index.html")


# ==========================================
# ANALYZE PAGE
# ==========================================

@app.route("/analyze")
def analyze():

    return render_template("analyze.html")


# ==========================================
# ANALYZE ARTICLE
# ==========================================

@app.route("/analyze", methods=["POST"])
def analyze_article():

    # ==========================================
    # USER INPUT
    # ==========================================

    article_text = request.form.get(
        "article_text",
        ""
    ).strip()

    article_url = request.form.get(
        "article_url",
        ""
    ).strip()

    article_file = request.files.get(
        "article_file"
    )

    publisher = "Not Available"

    publish_date = "Not Available"

    reputation = SourceReputation.analyze(
        article_url
    )

    clickbait = {

        "score": 0,

        "risk": "Low",

        "matches": []

    }

    bias = {

        "score": 0,

        "level": "Low",

        "matches": []

    }

    # ==========================================
    # FILE UPLOAD
    # ==========================================

    if article_file and article_file.filename:

        try:

            article_text = FileHandler.extract_text(
                article_file
            )

        except Exception as e:

            return render_template(

                "report.html",

                article="",

                summary="",

                prediction="UPLOAD ERROR",

                confidence=0,

                credibility=0,

                publisher=publisher,

                publish_date=publish_date,

                reputation=reputation,

                clickbait=clickbait,

                bias=bias,

                error_message=str(e)

            )

    # ==========================================
    # URL SCRAPING
    # ==========================================

    if article_url:

        try:

            scraped = NewsScraper.scrape(
                article_url
            )

            article_text = scraped["text"]

            publisher = MetadataExtractor.publisher(
                article_url
            )

            publish_date = MetadataExtractor.publication_date(
                scraped["publish_date"]
            )

            reputation = SourceReputation.analyze(
                article_url
            )

        except Exception as e:

            print("Scraper Error:", e)

    # ==========================================
    # VALIDATE ARTICLE
    # ==========================================

    if not article_text.strip():

        return render_template(

            "report.html",

            article="",

            summary="No article could be analyzed.",

            prediction="NO INPUT",

            confidence=0,

            credibility=0,

            publisher=publisher,

            publish_date=publish_date,

            reputation=reputation,

            clickbait=clickbait,

            bias=bias,

            error_message="""
Please provide one of the following:

• Paste a news article

• Enter a valid article URL

• Upload a TXT, PDF, or DOCX file.
"""

        )

    # ==========================================
    # CLEAN ARTICLE
    # ==========================================

    cleaned_text = TextCleaner.clean(
        article_text
    )

    # ==========================================
    # AI SUMMARY
    # ==========================================

    summary = ArticleSummarizer.summarize(
        article_text
    )

    # ==========================================
    # CLICKBAIT DETECTION
    # ==========================================

    clickbait = ClickbaitDetector.analyze(
        article_text
    )

    # ==========================================
    # BIAS DETECTION
    # ==========================================

    bias = BiasDetector.analyze(
        article_text
    )

    # ==========================================
    # AI PREDICTION
    # ==========================================

    predictor = FakeNewsPredictor()

    prediction = predictor.predict(
        cleaned_text
    )

    # ==========================================
    # EXPLAINABLE AI
    # ==========================================

    explainer = Explainability()

    explanation = explainer.explain(
        cleaned_text
    )

    # ==========================================
    # EXPLAINABLE AI
    # ==========================================

    #explanation = Explainability.explain(
    #    cleaned_text
    #)

    # ==========================================
    # CREDIBILITY SCORE
    # ==========================================

    credibility = CredibilityAnalyzer.calculate(

        prediction["confidence"]

    )

    # ==========================================
    # AI RECOMMENDATIONS
    # ==========================================

    recommendations = RecommendationGenerator.generate(

        prediction["prediction"],

        credibility,

        clickbait,

        bias,

        reputation

    )

    # ==========================================
    # SAVE ANALYSIS HISTORY
    # ==========================================

    record = HistoryManager.create_record(

        prediction=prediction["prediction"],

        confidence=prediction["confidence"],

        credibility=credibility,

        publisher=publisher,

        clickbait=clickbait,

        bias=bias

    )

    # ==========================================
    # SAVE TO HISTORY
    # ==========================================

    record = HistoryManager.create_record(

        prediction=prediction["prediction"],

        confidence=prediction["confidence"],

        credibility=credibility,

        publisher=publisher,

        clickbait=clickbait,

        bias=bias

    )

    HistoryManager.save(record)

    # ==========================================
    # REPORT
    # ==========================================

    return render_template(

        "report.html",

        article=article_text,

        summary=summary,

        prediction=prediction["prediction"],

        confidence=prediction["confidence"],

        credibility=credibility,

        publisher=publisher,

        publish_date=publish_date,

        reputation=reputation,

        clickbait=clickbait,

        bias=bias,

        recommendations=recommendations,

        explanation=explanation,

        error_message=None

    )


# ==========================================
# DASHBOARD
# ==========================================

@app.route("/dashboard")
def dashboard():

    analytics = DashboardAnalytics.generate()

    return render_template(

        "dashboard.html",

        analytics=analytics

    )


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )