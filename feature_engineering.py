import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# -----------------------------------
# LOAD PREPROCESSED DATA
# -----------------------------------
df = pd.read_csv("coffee_chatbot_preprocessed.csv")

X_text = df["clean_text"]
y = df["intent"]

# -----------------------------------
# TF-IDF VECTORIZATION
# -----------------------------------
tfidf = TfidfVectorizer(
    ngram_range=(1, 2),     # unigrams + bigrams
    max_features=5000      # control dimensionality
)

X = tfidf.fit_transform(X_text)

# -----------------------------------
# TRAIN-TEST SPLIT
# -----------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# -----------------------------------
# OUTPUT INFORMATION
# -----------------------------------
print("✅ Feature Engineering Completed")

print("\n📊 Feature Matrix Shape:")
print("X_train:", X_train.shape)
print("X_test :", X_test.shape)

print("\n🎯 Label Distribution (Train):")
print(y_train.value_counts())

# -----------------------------------
# SAVE OBJECTS FOR NEXT STEP
# -----------------------------------
import joblib

joblib.dump(tfidf, "tfidf_vectorizer.pkl")
joblib.dump((X_train, X_test, y_train, y_test), "ml_data.pkl")

print("\n✅ TF-IDF vectorizer and ML data saved")
