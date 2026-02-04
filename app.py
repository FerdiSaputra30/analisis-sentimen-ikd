from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

# Folder upload
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Kamus sentimen
positive_words = ["bagus", "baik", "mantap", "membantu", "mudah", "cepat"]
negative_words = ["buruk", "jelek", "error", "lambat", "susah", "tidak bisa", "kecewa"]

def analyze_sentiment(text):
    text = text.lower()
    pos = sum(word in text for word in positive_words)
    neg = sum(word in text for word in negative_words)

    if pos > neg:
        return "Positif"
    elif neg > pos:
        return "Negatif"
    else:
        return "Netral"

@app.route("/", methods=["GET", "POST"])
def index():
    reviews = []
    positif = negatif = netral = 0
    percent_pos = percent_neg = percent_net = 0
    conclusion = ""
    total = 0

    if request.method == "POST":
        file = request.files["file"]

        # Simpan file ke folder uploads
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Baca CSV
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                text = row["ulasan"]
                sentiment = analyze_sentiment(text)

                reviews.append({
                    "text": text,
                    "sentiment": sentiment
                })

                if sentiment == "Positif":
                    positif += 1
                elif sentiment == "Negatif":
                    negatif += 1
                else:
                    netral += 1

        total = positif + negatif + netral

        if total > 0:
            percent_pos = round((positif / total) * 100, 1)
            percent_neg = round((negatif / total) * 100, 1)
            percent_net = round((netral / total) * 100, 1)

            if negatif > positif:
                conclusion = "Mayoritas ulasan pengguna bersentimen negatif."
            elif positif > negatif:
                conclusion = "Mayoritas ulasan pengguna bersentimen positif."
            else:
                conclusion = "Sentimen ulasan pengguna cenderung netral."

    return render_template(
        "index.html",
        reviews=reviews,
        positif=positif,
        negatif=negatif,
        netral=netral,
        percent_pos=percent_pos,
        percent_neg=percent_neg,
        percent_net=percent_net,
        conclusion=conclusion,
        total=total
    )

if __name__ == "__main__":
    app.run(debug=True)