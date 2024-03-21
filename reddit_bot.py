# library called praw is used for making reddit bots
import praw 

reddit = praw.Reddit(
    client_id ='<client_id>',
    client_secret = "<client_secret>",
    user_agent = "MyBot/0.0.1"
)

# Login to reddit 
reddit.user.me()


# Get data from Reddit 
subreddit = reddit.subreddit("learnpython")
for submission in subreddit.hot(limit=5): # gets 5 items from the subreddit 
    if not submission.stickied:    
        print(f"Title :{submission.title}")
        print(f"Score :{submission.score}")
        print("------")
        
# additional features such as : 
# responding to comments 
# post new submissions 
# automate tasks

reddit.subreddit("test").submit(
    title = "First Reddit Bot",
    selftext = "Hi , I'm a Reddit bot created using Python."
)