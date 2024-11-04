from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os
from urllib.parse import urlparse
import reddit_connection
from reddit_api import scrape_reddit
from OpenAI_API import summarize_gaming_activity

app = Flask(__name__)
CORS(app)

reddit = reddit_connection.connection()

@app.route('/')
def index():
    return send_from_directory("Extension", "index.html")


@app.route('/subreddit-analysis', methods = ["GET"])
def subredditAnalysis():
    print("Analyzing Subreddit")
    user_data = scrape_reddit(10, 30)
    res = summarize_gaming_activity(user_data)
    return str(res)



if __name__ == '__main__':
    app.run(debug=True)