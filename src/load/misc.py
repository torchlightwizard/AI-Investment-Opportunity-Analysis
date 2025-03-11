import pandas as pd

def fill_blanks (df, company):
    if not df["sentiment"].eq("Positive").any():
        row = pd.DataFrame([[company, "Positive", 0]], columns=["company", "sentiment", "count"])
        df = pd.concat([df, row])
    if not df["sentiment"].eq("Neutral").any():
        row = pd.DataFrame([[company, "Neutral", 0]], columns=["company", "sentiment", "count"])
        df = pd.concat([df, row])
    if not df["sentiment"].eq("Negative").any():
        row = pd.DataFrame([[company, "Negative", 0]], columns=["company", "sentiment", "count"])
        df = pd.concat([df, row])
    return df