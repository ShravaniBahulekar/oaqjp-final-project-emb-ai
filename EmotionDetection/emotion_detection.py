import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Send the POST request
    response = requests.post(url, headers=headers, json=input_json)
    
    # Print the full response for debugging
    print("Full Response:", response.json())
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        response_json = response.json()
        
        # Extract scores for each emotion from the correct path
        emotion_data = response_json.get("emotionPredictions", [{}])[0].get("emotion", {})
        
        anger_score = emotion_data.get("anger", 0)
        disgust_score = emotion_data.get("disgust", 0)
        fear_score = emotion_data.get("fear", 0)
        joy_score = emotion_data.get("joy", 0)
        sadness_score = emotion_data.get("sadness", 0)

        # Determine the dominant emotion
        scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(scores, key=scores.get)

        # Format the output as specified
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    else:
        # Handle errors
        return {"error": response.text}
