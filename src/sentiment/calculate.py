from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException

LABELS_EN = {0: -1, 1: 0, 2: 1}
tokenizer_en = None
model_en = None
tokenizer_all = None
model_all = None



def map_multilingual_label(label):
    if label in {1, 2}:
        return -1
    if label == 3:
        return 0
    if label in {4, 5}:
        return 1



def load_models():
    """Loads models only when first needed."""

    global tokenizer_en, model_en, tokenizer_all, model_all
    if tokenizer_en is None:
        tokenizer_en = AutoTokenizer.from_pretrained("finiteautomata/bertweet-base-sentiment-analysis")
        model_en = AutoModelForSequenceClassification.from_pretrained("finiteautomata/bertweet-base-sentiment-analysis")
        model_en.eval().to("cpu")
    
    if tokenizer_all is None:
        tokenizer_all = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
        model_all = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
        model_all.eval().to("cpu")



def calculate_sentiment(sentence):
    """Choose prediction model."""

    try:
        load_models()
        lang = detect(sentence)
        if lang == "en":
            return calculate_sentiment_english(sentence)
        return calculate_sentiment_all(sentence)
    except LangDetectException as err:
        print(f"Fucntion: calculate_sentiment. Language Detection Error: {err}")
    except Exception as err:
        print(f"Function: calculate_sentiment. Unexpected Error: {err}")
    return 0



def calculate_sentiment_english(sentence):
    """Predict sentiment (-1=Negative, 0=Neutral, 1=Positive) using the English model."""

    inputs = tokenizer_en(sentence, return_tensors="pt", truncation=True, padding=True).to("cpu")
    with torch.no_grad():
        logits = model_en(**inputs).logits.to(torch.float16)
    predicted_class = torch.argmax(logits).item()
    return LABELS_EN[predicted_class]



def calculate_sentiment_all(sentence):
    """Predict sentiment (-1=Negative, 0=Neutral, 1=Positive) using the multilingual model."""

    inputs = tokenizer_all(sentence, return_tensors="pt", truncation=True, padding=True).to("cpu")
    with torch.no_grad():
        logits = model_all(**inputs).logits.to(torch.float16)
    predicted_class = torch.argmax(logits).item() + 1
    return map_multilingual_label(predicted_class)



if __name__ == "__main__":
    print(calculate_sentiment("I love this!"))  # English → 1 (Positive)
    print(calculate_sentiment("¡Me encanta esto!"))  # Spanish → 1 (Positive)
    print(calculate_sentiment("Das ist schrecklich!"))  # German → -1 (Negative)