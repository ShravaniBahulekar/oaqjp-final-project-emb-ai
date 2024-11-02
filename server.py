from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_endpoint():
    data = request.json
    text_to_analyze = data.get('text')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    response_message = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    )
    return response_message

if __name__ == "__main__":
    app.run(debug=True, port=5000)
