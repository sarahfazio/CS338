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

    #TODO: handle case where we are not on a subreddit nor user page
    subreddit_name = request.args.get('subreddit')
    sort= request.args.get('sort')

    print(f"Analyzing the {subreddit_name} subreddit sorting by {sort}")
    

    user_data = scrape_reddit(10, 30, sort = sort, subreddit_name = subreddit_name)
    res = summarize_gaming_activity(user_data)
    return jsonify({"message": res})



if __name__ == '__main__':
    app.run(debug=True)