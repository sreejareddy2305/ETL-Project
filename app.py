from flask import Flask,request,render_template
import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torch.nn import functional as F

app = Flask(__name__)


# Define constants
PRETRAINED_MODEL_NAME = "bert-base-uncased"
MODEL_SAVE_PATH = "bert_fake_job_posting_model.pt"
MAX_LEN = 128

# Load model and tokenizer
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = BertForSequenceClassification.from_pretrained(
    PRETRAINED_MODEL_NAME,
    num_labels=2
)

# FIX: add strict=False
model.load_state_dict(
    torch.load(MODEL_SAVE_PATH, map_location=device),
    strict=False
)

model.to(device)
model.eval()

tokenizer = BertTokenizer.from_pretrained(PRETRAINED_MODEL_NAME)


@app.route('/')
def home():
    return render_template('index.html',prediction=None)

@app.route('/predict',methods = ['POST'])
def predict():
    if request.method == 'POST':

        title = request.form['title']
        description = request.form['description']
        requirement = request.form['requirement']
        text = title + description+requirement

        encoding = tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=MAX_LEN,
            return_token_type_ids=False,
            truncation=True,
            padding="max_length",
            return_attention_mask=True,
            return_tensors="pt",
        )

        input_ids = encoding["input_ids"].to(device)
        attention_mask = encoding["attention_mask"].to(device)

        with torch.no_grad():
            outputs = model(input_ids, attention_mask=attention_mask)
            logits = outputs.logits
            probabilities = F.softmax(logits, dim=1).cpu().numpy()
            predicted_label = torch.argmax(logits, dim=1).item()

        # Generate output message
        confidence = round(max(probabilities[0]) * 100, 2)
        if predicted_label == 1:
            message = f"This Job Posting is predicted as FAKE with {confidence}% confidence."
        else:
            message = f"This Job Posting is predicted as REAL with {confidence}% confidence."

        return render_template('result.html',message=message)

if __name__=="__main__":
    app.run(debug=True)