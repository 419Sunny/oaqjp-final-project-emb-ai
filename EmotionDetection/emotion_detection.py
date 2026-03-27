"""
Emotion detection module using Watson NLP library with error handling
"""

import requests
import json

def emotion_detector(text_to_analyze):
    """
    Sends text to Watson NLP API and returns formatted emotion analysis results
    
    Args:
        text_to_analyze (str): Text to analyze for emotions
    
    Returns:
        dict: Dictionary containing emotion scores and dominant emotion
              Returns None values for all keys when status code is 400
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, headers=headers, json=input_json)
    
    # Error handling for blank entries (status code 400)
    if response.status_code == 400:
        # Return dictionary with all values set to None
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Process successful response (status code 200)
    elif response.status_code == 200:
        # Parse the JSON response
        response_dict = json.loads(response.text)
        
        # Extract emotions from the response
        emotions = response_dict['emotionPredictions'][0]['emotion']
        
        # Find the dominant emotion (emotion with highest score)
        dominant_emotion = max(emotions, key=emotions.get)
        
        # Format the output as required
        formatted_output = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }
        
        return formatted_output
    
    # Handle other status codes
    else:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
