import pandas as pd

def calculate_harm_index(df):
    total = len(df)
    toxic_pct = df['toxic'].mean() * 100
    misinfo_pct = df['misinfo'].mean() * 100
    selfharm_pct = df['selfharm'].mean() * 100
    return {
        "toxic": toxic_pct,
        "misinfo": misinfo_pct,
        "selfharm": selfharm_pct,
        "total": total
    }
