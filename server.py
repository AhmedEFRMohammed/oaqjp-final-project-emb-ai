"""
This is a flask server for a web app frontend that takes
texts from users, delivers it to IBM's Watson NLP library's 
Emotion Detect function, and the returns tthe result to
the front-end for the user to observe
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    """
    This is the handling function for the API endpoint that 
    receives the request query to conduct emotion decetion on it.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    formatted_response = f"For the given statement, the system response is \
    'anger': {response['anger']}, 'disgust': {response['disgust']}, \
    'fear': {response['fear']}, 'joy': {response['joy']} and \
    'sadness': {response['sadness']}. The dominant emotion is \
    {response['dominant_emotion']}."
    return formatted_response

@app.route("/")
def render_index_page():
    """
    This is the handling function for the API endpoint that
    delivers the landing page once the user visit the website
    """
    return render_template("index.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
