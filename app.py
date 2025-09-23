from flask import Flask, request, jsonify, render_template
from generate_tweet import create_tweet, create_compare_tweets_with_gemini_models

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_tweet', methods=['POST'])
def generate_tweet():
    data = request.get_json()
    if 'prompt' not in data:
        return jsonify({"error": "Missing 'prompt' in request body"}), 400

    result = create_tweet(data['prompt'])
    if result is None:
        return jsonify({"error": "No top tweets found for engagement type"}), 404

    return jsonify(result), 200

@app.route('/compare_tweets', methods=['POST'])
def compare_tweets():
    # Expecting JSON body with 'analysed_tweets' key that is a list
    data = request.get_json()
    if 'prompt' not in data:
        return jsonify({"error": "Missing 'prompt' in request body"}), 400

    # Modify your compare function to return results as a dict,
    # or accumulate necessary output and return it here.
    output = create_compare_tweets_with_gemini_models(data['prompt'])

    if output is None:
        return jsonify({"error": "Could not perform tweet comparison"}), 500

    return jsonify(output), 200

if __name__ == '__main__':
    app.run(debug=True)
