from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os
import json
from urllib.parse import urlparse
from reddit_api import scrape_reddit, scrape_user_posts
from OpenAI_API import summarize_gaming_activity, summarize_user_profile

app = Flask(__name__)
CORS(app)

# Global path for the stored file (only one file will be stored)
stored_file_path = "stored_data/user_profile.json"
username_stored = False


@app.route('/')
def index():
    return send_from_directory("Extension", "index.html")


@app.route('/subreddit-analysis', methods = ["GET"])
def subredditAnalysis():
    subreddit_name = request.args.get('subreddit')
    sort= request.args.get('sort')

    print(f"Analyzing the {subreddit_name} subreddit sorting by {sort}")
    

    user_data = scrape_reddit(10, 30, sort = sort, subreddit_name = subreddit_name)

    #TODO: add check that the profile exists
    print("summarize gaming activity")
    res = summarize_gaming_activity(user_data, get_stored_analysis().get_json(), username_stored)
    return jsonify({"message": res})

@app.route('/user-analysis', methods=["GET"])
def userAnalysis():
    global username_stored
    username = request.args.get('username')
    stored = request.args.get('stored')

    print("this request was ",stored, type(stored))

    if not username:
        return jsonify({"error": "Username is required"}), 400

    try:
        # Fetch user data
        user_data = scrape_user_posts(username, num_posts=10, sort="new")
        # Summarize or process the data if needed
        res = summarize_user_profile(user_data)

        if stored == "True":
            # Save to a single JSON file for later use (overwriting if exists)
            os.makedirs(os.path.dirname(stored_file_path), exist_ok=True)
            with open(stored_file_path, 'w') as f:
                json.dump(res, f, indent=4)
            
            username_stored = True

            return jsonify({"message": res, "stored": True})

        return jsonify({"message": res})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def get_stored_analysis():
    try:
        if os.path.exists(stored_file_path):
            with open(stored_file_path, 'r') as f:
                stored_data = json.load(f)
            return jsonify({"message": stored_data, "stored": True})
        else:
            return jsonify({"error": "No stored data found."}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)