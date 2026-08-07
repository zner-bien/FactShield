import os
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.naive_bayes import MultinomialNB

from sklearn.svm import LinearSVC

from sklearn.metrics import (
    accuracy_score,
    classification_report
)

import re
import string
import pandas as pd
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# ==========================================
# DOWNLOAD NLTK RESOURCES
# ==========================================

nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")


# ==========================================
# INITIALIZE NLP TOOLS
# ==========================================

stop_words = set(stopwords.words("english"))

lemmatizer = WordNetLemmatizer()


# ==========================================
# TEXT CLEANING FUNCTION
# ==========================================

def clean_text(text):

    text = str(text)

    # Convert to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove HTML tags
    text = re.sub(r"<.*?>", "", text)

    # Remove punctuation
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    # Remove numbers
    text = re.sub(r"\d+", "", text)

    words = []

    for word in text.split():

        if word not in stop_words:

            word = lemmatizer.lemmatize(word)

            words.append(word)

    return " ".join(words)


# ==========================================
# LOAD DATASETS
# ==========================================

print("\nLoading datasets...\n")

fake_df = pd.read_csv("datasets/Fake.csv")

true_df = pd.read_csv("datasets/True.csv")


# ==========================================
# ADD LABELS
# ==========================================

fake_df["label"] = 0

true_df["label"] = 1


# ==========================================
# MERGE DATASETS
# ==========================================

df = pd.concat(
    [fake_df, true_df],
    ignore_index=True
)


# ==========================================
# SHUFFLE DATASET
# ==========================================

df = df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)


# ==========================================
# CREATE ONE TEXT COLUMN
# ==========================================

print("Combining title and article text...\n")

df["content"] = (
    df["title"].fillna("")
    + " "
    + df["text"].fillna("")
)


# ==========================================
# CLEAN ARTICLES
# ==========================================

print("Cleaning articles...")

df["content"] = df["content"].apply(clean_text)

print("Cleaning Complete!\n")


# ==========================================
# DATASET INFORMATION
# ==========================================

print("=" * 60)

print("DATASET INFORMATION")

print("=" * 60)

print(f"\nDataset Shape: {df.shape}")

print("\nClass Distribution:\n")

print(df["label"].value_counts())

print("\nColumns:\n")

print(df.columns)

print("\nFirst Five Rows:\n")

print(df.head())


# ==========================================
# SAMPLE CLEANED ARTICLES
# ==========================================

print("\n" + "=" * 60)

print("SAMPLE CLEANED ARTICLES")

print("=" * 60)

for i in range(5):

    print(f"\nArticle {i + 1}")

    print("-" * 60)

    print(df["content"].iloc[i][:500])

print("\n\nPreprocessing completed successfully!")

# ==========================================
# TF-IDF VECTORIZATION
# ==========================================

print("\nCreating TF-IDF features...\n")

vectorizer = TfidfVectorizer(

    max_features=5000,

    stop_words="english"

)

X = vectorizer.fit_transform(df["content"])

y = df["label"]

print("TF-IDF Completed!")

print("\nFeature Matrix Shape:")

print(X.shape)

# ==========================================
# TRAIN TEST SPLIT
# ==========================================

print("\nSplitting dataset...\n")

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42

)

print("Training Samples :", X_train.shape)

print("Testing Samples  :", X_test.shape)

# ==========================================
# LOGISTIC REGRESSION
# ==========================================

print("\nTraining Logistic Regression...\n")

lr = LogisticRegression(

    max_iter=1000

)

lr.fit(

    X_train,

    y_train

)

pred_lr = lr.predict(

    X_test

)

acc_lr = accuracy_score(

    y_test,

    pred_lr

)

print("Logistic Regression Accuracy:")

print(round(acc_lr * 100, 2), "%")

# ==========================================
# MULTINOMIAL NAIVE BAYES
# ==========================================

print("\nTraining Naive Bayes...\n")

nb = MultinomialNB()

nb.fit(

    X_train,

    y_train

)

pred_nb = nb.predict(

    X_test

)

acc_nb = accuracy_score(

    y_test,

    pred_nb

)

print("Naive Bayes Accuracy:")

print(round(acc_nb * 100, 2), "%")

# ==========================================
# LINEAR SVM
# ==========================================

print("\nTraining Linear SVM...\n")

svm = LinearSVC()

svm.fit(

    X_train,

    y_train

)

pred_svm = svm.predict(

    X_test

)

acc_svm = accuracy_score(

    y_test,

    pred_svm

)

print("Linear SVM Accuracy:")

print(round(acc_svm * 100, 2), "%")

# ==========================================
# MODEL COMPARISON
# ==========================================

print("\n" + "=" * 60)
print("MODEL COMPARISON")
print("=" * 60)

results = {
    "Logistic Regression": acc_lr,
    "Naive Bayes": acc_nb,
    "Linear SVM": acc_svm
}

for model, score in results.items():
    print(f"{model:<25}: {score * 100:.2f}%")

best_model_name = max(results, key=results.get)

print("\nBest Model:")

print(best_model_name)

# ==========================================
# SAVE BEST MODEL
# ==========================================

os.makedirs("trained_models", exist_ok=True)

if best_model_name == "Logistic Regression":
    best_model = lr

elif best_model_name == "Naive Bayes":
    best_model = nb

else:
    best_model = svm


joblib.dump(
    best_model,
    "trained_models/factshield_model.pkl"
)

joblib.dump(
    vectorizer,
    "trained_models/tfidf_vectorizer.pkl"
)

print("\nModel saved successfully!")

print("Location: trained_models/")

