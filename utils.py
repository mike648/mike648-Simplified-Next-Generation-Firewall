import subprocess
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import spacy
from transformers import pipeline

nlp = spacy.load("en_core_web_sm")
sia = SentimentIntensityAnalyzer()
classifier = pipeline('sentiment-analysis')

def analyze_log_entry(log_entry):
    doc = nlp(log_entry.message)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    sentiment = sia.polarity_scores(log_entry.message)
    return entities, sentiment

def classify_alert(alert_message):
    return classifier(alert_message)

def run_ips(packet):
    # using Suricata
    with open('/tmp/packet.pcap', 'wb') as f:
        f.write(packet.raw_data)
    result = subprocess.run(['suricata', '-r', '/tmp/packet.pcap'], capture_output=True)
    return result.returncode == 0