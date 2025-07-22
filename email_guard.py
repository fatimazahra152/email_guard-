import sys
import json
from transformers import pipeline


classifier = pipeline(
    "text-classification",
    model="mrm8488/bert-tiny-finetuned-sms-spam-detection",
    top_k=1,
    truncation=True,
    max_length=512 
)

def classify_email(text):
    result = classifier(text)[0][0]
    label = result['label']
    score = result['score']

    if label == "LABEL_1": 
        classification = "spam"
    elif label == "LABEL_0": 
        classification = "legit"
    else: 
        classification = "unknown"

    return {
        "classification": classification,
        "confidence": round(score, 2),
        "explanation": f"Predicted '{label}' with score {round(score, 2)}"
    }

if __name__ == "__main__":
    input_text = " ".join(sys.argv[1:])
    result = classify_email(input_text)
    print(json.dumps(result, indent=2))