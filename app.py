from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os
from urllib.parse import urlparse
from reddit_api import scrape_reddit, scrape_user_posts
from OpenAI_API import summarize_gaming_activity, summarize_user_profile

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return send_from_directory("Extension", "index.html")


@app.route('/subreddit-analysis', methods = ["GET"])
def subredditAnalysis():
    subreddit_name = request.args.get('subreddit')
    sort= request.args.get('sort')

    print(f"Analyzing the {subreddit_name} subreddit sorting by {sort}")
    

    user_data = scrape_reddit(10, 30, sort = sort, subreddit_name = subreddit_name)
    res = summarize_gaming_activity(user_data)
    return jsonify({"message": res})

@app.route('/user-analysis', methods=["GET"])
def userAnalysis():
    username = request.args.get('username')

    if not username:
        return jsonify({"error": "Username is required"}), 400

    try:
        # Fetch user data
        user_data = scrape_user_posts(username, num_posts=10, sort="new")
        # Summarize or process the data if needed
        res = summarize_user_profile(user_data)
        return jsonify({"message": res})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)