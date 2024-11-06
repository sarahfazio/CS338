import praw
import numpy
from api_connections import reddit_connection
from OpenAI_API import summarize_gaming_activity
import time

reddit = reddit_connection()

def scrape_reddit(num_subreddit_posts, num_user_posts, sort = "hot", subreddit_name = "Minecraft"):
    #subreddit_name = input("Input the name of the subreddit you're interested in: ")
    before = time.time()

    # TODO: input validation
    subreddit = reddit.subreddit(subreddit_name)

    users = []  # List to hold user dictionaries

    subreddit_submissions = subreddit.hot(limit=num_subreddit_posts)
    if sort == "hot":
        subreddit_submissions = subreddit.hot(limit=num_subreddit_posts)
    elif sort == "top":
        subreddit_submissions = subreddit.top()
    elif sort == "new":
        subreddit_submissions = subreddit.new(limit=num_subreddit_posts)

    for submission in subreddit_submissions:
        user_info = {}
        
        # Check if the author exists
        if submission.author:
            username = submission.author.name  # Get the username
            user_info['username'] = username
            
            # Create a Redditor object using the username
            redditor1 = reddit.redditor(username)

            # Fetch top submissions from the user
            user_submissions = []
            submissions = list(redditor1.submissions.hot(limit=num_user_posts))
            if sort == "hot":
                submissions = list(redditor1.submissions.hot(limit=num_user_posts))
            if sort == "top":
                submissions = list(redditor1.submissions.top(limit=num_user_posts))
            if sort == "new":
                submissions = list(redditor1.submissions.new(limit=num_user_posts))
            for user_submission in submissions:
                user_submissions.append({
                    'title': user_submission.title,
                    'score': user_submission.score,
                    'body': user_submission.selftext,
                    'subreddit': user_submission.subreddit.display_name,
                    'url': user_submission.url
                })

            user_info['submissions'] = user_submissions
        else:
            user_info['username'] = '[deleted]'
            user_info['submissions'] = []

        # Append user info to the users list
        users.append(user_info)

    print(f"The call took {time.time() - before} seconds and returned {num_subreddit_posts * num_user_posts} submissions.")
    return users  # Return the list of users

# Example usage
if __name__ == "__main__":
    user_data = scrape_reddit(10, 30)
    print(summarize_gaming_activity(user_data))  # You can print or use this list as needed