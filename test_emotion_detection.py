import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_joy(self):
        result = emotion_detector("I love sunny days and warm hugs!")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_sadness(self):
        result = emotion_detector("I feel so lost and hopeless.")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_anger(self):
        result = emotion_detector("I'm really furious and upset about the situation.")
        self.assertEqual(result['dominant_emotion'], 'anger')

if __name__ == '__main__':
    unittest.main()
