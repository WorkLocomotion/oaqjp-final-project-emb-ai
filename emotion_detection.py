import requests

def emotion_detector(text_to_analyze):
    # Define the API endpoint
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    # Define the request headers
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Prepare the input JSON
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send the POST request
    response = requests.post(url, json=payload, headers=headers)

    # Return the raw response text
    return response.text
