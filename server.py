"""
Flask web server for Emotion Detection application with error handling
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
    Process text input and return emotion analysis with error handling
    Accepts POST requests with text field
    """
    text_to_analyze = request.form['text']
    
    # Check for blank input
    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please try again!"
    
    # Call the emotion_detector function
    result = emotion_detector(text_to_analyze)
    
    # Check if the result has None values (error case)
    if result is None or result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    
    # Format the response for valid input
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
