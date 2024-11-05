import praw


def connection():
   return praw.Reddit(
       client_id="zgB3T7sYH_rJbWpK6yFrag",
       client_secret="02Wfh-SN-4srUl1qkx6oG6-jpR4yEQ",
       user_agent="my user agent",
   )
