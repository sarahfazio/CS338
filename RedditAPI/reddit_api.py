import praw
import numpy

import reddit_connection

reddit = reddit_connection.connection()
print(reddit.read_only)

#for submission in reddit.subreddit("reddeadredemption").hot(limit=10):
    #print(submission.title)

# assume you have a praw.Reddit instance bound to variable `clipseclipsey`
redditor1 = reddit.redditor("Limp_Resolution_1722")
print(redditor1.link_karma)

try:
    redditor1.comments.top(limit=1)  # Check if comments exist
    print("User found. Fetching comments and posts...\n")
except Exception as e:
    print(f"Error fetching user: {e}")

# Iterate through the top comments from the last year and print their bodies
comments = list(redditor1.comments.top(limit=None))  # Convert to list

for comment in comments[1:10]:
    print(f"Comment ID: {comment.id}")
    print(f"Score: {comment.score}")
    print(f"Body: {comment.body}\n")

#Iterate through the posts
submissions =  list(redditor1.submissions.top(limit = None))
for submission in submissions[1:10]:
    print(f"Title: {submission.title}")
    print(f"Score: {submission.score}")
    print(f"Body: {submission.selftext}")
    print(f"URL: {submission.url}\n")

print(len(comments), len(submissions))