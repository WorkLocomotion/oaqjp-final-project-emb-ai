"""
Flask application for detecting emotion from text input using Watson NLP service.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """Render the main HTML page."""
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_analyzer():
    """Handle emotion detection request from the frontend."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid input! Try again."

    emotion = response["dominant_emotion"]
    score = response[emotion]

    return f"The given text has been identified as {emotion} with a score of {score}."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
