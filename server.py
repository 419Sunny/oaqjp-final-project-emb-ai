"""
Flask web server for Emotion Detection application
Provides a web interface for emotion analysis
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """
    Process text input and return emotion analysis
    Accepts POST requests with text field
    """
    text_to_analyze = request.form['text']
    
    # Call the emotion_detector function
    result = emotion_detector(text_to_analyze)
    
    # Format the response
    if result:
        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']}, "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
        return response_text
    else:
        return "Error: Unable to process the request."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)