# models/load_model.py
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import streamlit as st

@st.cache_resource  # cache the model so it loads only once
def load_classifier():
    # Use DistilBERT tokenizer + Unitary toxic-bert model
    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
    model = AutoModelForSequenceClassification.from_pretrained("unitary/toxic-bert")

    # Force CPU (device=-1)
    classifier = pipeline(
        "text-classification",
        model=model,
        tokenizer=tokenizer,
        device=-1   # ensure it runs on CPU only
    )
    return classifier
