import requests  # Import the requests library for making HTTP requests
import json  # Import the json library for handling JSON data

def emotion_detector(text_to_analyse):
    # URL for the Watson Emotion Predict API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Headers required for the API request
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # JSON payload for the API request, including the text to analyze
    payload = {
        "raw_document": {
            "text": text_to_analyse  # The text to analyze
        }
    }

    # Sending a POST request to the Watson API
    response = requests.post(url, json=payload, headers=headers)

    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Convert the response text to a dictionary
        response_data = json.loads(response.text)

        # Extract the first set of emotion predictions
        emotion_predictions = response_data.get('emotionPredictions', [])
        
        if emotion_predictions:
            # Extract the emotions and their scores from the first prediction
            emotions = emotion_predictions[0].get('emotion', {})
            anger_score = emotions.get('anger', 0)
            disgust_score = emotions.get('disgust', 0)
            fear_score = emotions.get('fear', 0)
            joy_score = emotions.get('joy', 0)
            sadness_score = emotions.get('sadness', 0)

            # Create a dictionary with all the emotions and scores
            emotion_scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
            }

            # Find the dominant emotion based on the highest score
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)

            # Add the dominant emotion to the dictionary
            emotion_scores['dominant_emotion'] = dominant_emotion

            # Return the formatted output
            return emotion_scores

        else:
            print("No emotion predictions found in the response.")
            return None

    else:
        # Print the error if the request failed
        print(f"Error: {response.status_code}")
        print(f"Response: {response.text}")
        return None  # Return None in case of an error
