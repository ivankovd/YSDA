from flask import Flask, render_template, request
from werkzeug import secure_filename
import os
from werkzeug.serving import WSGIRequestHandler
import logging
from sentiment_models import SentimentClassifier


logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
    level=logging.INFO)

app = Flask(__name__)

model = SentimentClassifier()

@app.route("/sentiment_analysis", methods=["POST", "GET"])
def index_page(text="", prediction_message=""):
    if request.method == "POST":
        text = request.form["text"]
        score, score_color = model.run(text)
        
    else:
        text, score, score_color = None, None, None
    return render_template('index.html', text=text, score=score, score_color=score_color)


if __name__ == "__main__":
    
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(host='0.0.0.0', port=5000, debug=False)