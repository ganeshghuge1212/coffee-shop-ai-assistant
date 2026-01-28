import random
import numpy as np
import joblib
from preprocess import clean_text

# -----------------------------------
# LOAD TRAINED MODEL & VECTORIZER
# -----------------------------------
model = joblib.load("intent_classifier.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# -----------------------------------
# CONFIGURATION
# -----------------------------------
CONFIDENCE_THRESHOLD = 0.60
MIN_WORDS_REQUIRED = 2   # VERY IMPORTANT

FALLBACK_MESSAGES = [
    "Sorry, I didn't quite understand that ☕",
    "I'm not trained on that yet. Can I help with our coffee menu?",
    "Could you please rephrase your question?",
    "I can help with menu, prices, or coffee recommendations 😊"
]

# -----------------------------------
# SAFE INTENT PREDICTION
# -----------------------------------
def predict_intent_safe(user_input: str):
    # -------- STEP 1: PREPROCESS --------
    cleaned = clean_text(user_input)

    # -------- STEP 2: EMPTY / SHORT INPUT CHECK --------
    if not cleaned or len(cleaned.split()) < MIN_WORDS_REQUIRED:
        return None, 0.0

    # -------- STEP 3: VECTORIZE --------
    X = vectorizer.transform([cleaned])

    # -------- STEP 4: CONFIDENCE CHECK --------
    probabilities = model.predict_proba(X)[0]
    max_confidence = float(np.max(probabilities))
    predicted_intent = model.classes_[int(np.argmax(probabilities))]

    if max_confidence < CONFIDENCE_THRESHOLD:
        return None, max_confidence

    return predicted_intent, max_confidence


# -----------------------------------
# FINAL RESPONSE FUNCTION (OPTIONAL BUT BEST)
# -----------------------------------
def get_safe_response(user_input: str, intent_responses: dict):
    intent, confidence = predict_intent_safe(user_input)

    if intent is None:
        return random.choice(FALLBACK_MESSAGES)

    return random.choice(intent_responses[intent])
