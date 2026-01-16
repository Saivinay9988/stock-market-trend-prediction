from flask import Flask, request, render_template
from textblob import TextBlob

app = Flask(__name__)

def predict_trend(news):
    analysis = TextBlob(news)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "UP 📈"
    else:
        return "DOWN 📉"

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = ""
    if request.method == "POST":
        news = request.form["news"]
        prediction = predict_trend(news)
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
