from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector  # Import the emotion_detector function from the package

app = Flask(__name__)  # Initialize Flask application

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    # Extract the input text from the POST request
    data = request.json
    text_to_analyse = data.get('text', '')

    # Call the emotion detector function
    if text_to_analyse:
        result = emotion_detector(text_to_analyse)

        # Format the result as required
        formatted_result = (
            f"For the given statement, the system response is 'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
            f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )

        # Return the formatted response as JSON
        return jsonify({
            "result": formatted_result
        })
    else:
        return jsonify({
            "error": "No text provided"
        }), 400

# Run the Flask application on localhost:5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
