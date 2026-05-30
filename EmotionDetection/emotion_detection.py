import json
import requests
"""
This module uses IBM Watson NLP library's function for emotion detection
"""

def emotion_detector(text_to_analyze):
    """
    This function receives a text, and uses the Emotion Predict function of Watson NLP
    """
    url ='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url=url, headers=headers, json=input_json, timeout=5)
    
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotions = formatted_response["emotionPredictions"][0]["emotion"]

        dominant_emotion = ""
        dominant_emotion_Score = 0

        for k, v in emotions.items():
            if v > dominant_emotion_Score:
                dominant_emotion_Score = v
                dominant_emotion = k

        return {**emotions, "dominant_emotion": dominant_emotion}
    elif response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion":None
            }
    elif response.status_code == 500:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion":None
            }
    else:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion":None
            }
        


