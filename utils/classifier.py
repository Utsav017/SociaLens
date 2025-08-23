# utils/classifier.py
def classify_text(text, toxic_model):
    categories = {"toxic": False, "misinfo": False, "selfharm": False}

    # Toxic check (model-based)
    pred = toxic_model(text)[0]
    if pred['label'].lower() in ['toxic', 'insult', 'hate'] and pred['score'] > 0.7:
        categories["toxic"] = True

    # Misinformation keywords (rule-based for MVP)
    misinfo_keywords = ["fake news", "hoax", "rumor", "misinformation", "not true"]
    if any(kw in text.lower() for kw in misinfo_keywords):
        categories["misinfo"] = True

    # Self-harm keywords (rule-based)
    selfharm_keywords = ["suicidal", "kill myself", "end my life", "depressed", "i want to die"]
    if any(kw in text.lower() for kw in selfharm_keywords):
        categories["selfharm"] = True

    return categories
