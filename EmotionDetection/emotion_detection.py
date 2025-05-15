import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            formatted_response = json.loads(response.text)
            emotions = formatted_response["emotionPredictions"][0]["emotion"]
            dominant_emotion = max(emotions, key=emotions.get)
            return {
                "anger": emotions["anger"],
                "disgust": emotions["disgust"],
                "fear": emotions["fear"],
                "joy": emotions["joy"],
                "sadness": emotions["sadness"],
                "dominant_emotion": dominant_emotion
            }
        else:
            # Handle non-200 (e.g., 500) responses
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }

    except Exception:
        # Handle network errors or unexpected issues
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
