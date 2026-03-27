"""
Unit tests for Emotion Detection module
Tests the emotion_detector function with various text inputs
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """Test cases for emotion detection functionality"""
    
    def test_joy_detection(self):
        """
        Test case 1: Verify joy emotion detection
        Statement: "I am glad this happened"
        Expected dominant emotion: joy
        """
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')
    
    def test_anger_detection(self):
        """
        Test case 2: Verify anger emotion detection
        Statement: "I am really mad about this"
        Expected dominant emotion: anger
        """
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')
    
    def test_disgust_detection(self):
        """
        Test case 3: Verify disgust emotion detection
        Statement: "I feel disgusted just hearing about this"
        Expected dominant emotion: disgust
        """
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')
    
    def test_sadness_detection(self):
        """
        Test case 4: Verify sadness emotion detection
        Statement: "I am so sad about this"
        Expected dominant emotion: sadness
        """
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')
    
    def test_fear_detection(self):
        """
        Test case 5: Verify fear emotion detection
        Statement: "I am really afraid that this will happen"
        Expected dominant emotion: fear
        """
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()