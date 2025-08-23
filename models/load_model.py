# models/load_model.py
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

def load_classifier():
    # Hindi + English capable baseline (IndicBERT is for later fine-tuning)
    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
    model = AutoModelForSequenceClassification.from_pretrained("unitary/toxic-bert")
    classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)
    return classifier
