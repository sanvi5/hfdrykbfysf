# import the necessary modules
from flask import Flask, render_template, request, jsonify
import sentiment_analysis as sa

app = Flask(__name__)

# app route for index page
@app.route('/')
def home():
    return render_template('index.html')

# write a route for post request
@app.route('/review', methods=['POST'])
def review():
    # extract the customer_review by writing the appropriate 'key' from the JSON data
    data = request.get_json()
    review = data.get('customer_review')

    # check if the customer_review is empty, return error
    if not review:
        return jsonify({'status': 'error', 'message': 'Empty response'})


    else:
        sentiment, image_path = sa.predict(review)
        return jsonify({'sentiment': sentiment, 'image_path': image_path})

if __name__ == "__main__":
    app.run(debug=True)
