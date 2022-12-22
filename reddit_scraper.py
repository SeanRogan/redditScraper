import private
import praw
import dataset
import settings

client_id = private.CLIENT_ID
client_secret = private.CLIENT_SECRET
user_agent = private.USER_AGENT
# create a database object
db = dataset.connect(private.DB_CONNECTION_STRING)

# create a reddit client
redditClient = praw.Reddit(
    client_id,
    client_secret,
    user_agent,
)

subreddits = dict()
# for redditClient

# find all subreddits associated with the search terms in settings
for search_term in settings.SUBREDDITS:
    list_of_subs = redditClient.subreddits.search(search_term)  # get subreddits associated with that search term
    subreddits[search_term] = list_of_subs                      # add the key : value pair search_term : subreddits[] to the subreddits dictionary


# go through subreddits dict, for each subreddit...
# get the top 100 newest submissions from the subreddit and save them to an array.
# save that array to a new dict subreddit_content with k:v being subreddit:array of submissions
subreddit_content = dict()
for sub in subreddits:
    submissions_list = []
    for submission in redditClient.subreddit(sub).new():
        submissions_list.append(submission)
    subreddit_content[sub] = submissions_list

# the dict should now have all submissions from all subreddits searched.


# ITERATE OVER EACH ONE AND PULL THE POSTS AND FORMAT AND STORE THEM AS YOU LOOP

def collect_post(self, post):
    pass
