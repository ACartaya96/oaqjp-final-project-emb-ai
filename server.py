"""
This server module uses Flask to help connect the emotion detection
module to your full web app development. Dependencies include IBM Watson's NLP Emotion
Prediction API
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def emo_detector():
    """
    emo_detector grabs request argument from MyWebScript and runs it through
    our emotion_detector function imported from the EmotionDetection package.
    It will then extract the data and respond to the user its confidence score, or
    an Invalid if nothing was put into the input.
    """
    # Retrieving text from request argument for analysis
    text_to_analyse = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyse)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant = response['dominant_emotion']

    if response['dominant_emotion'] is None:
        return "Invalid input! Try again."

    return f'''For the given statement, the system response is
        'anger': {anger}, 'disgust': {disgust},
        'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}.
        The dominant emotion is {dominant}.'''


@app.route("/")
def render_index_page():
    """
    This render_index_page helps render the html template for our application
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    