import private
import praw
import dataset
import settings

# create a database object
db = dataset.connect(private.DB_CONNECTION_STRING)

# create a reddit client
redditClient = praw.Reddit(client_id=private.CLIENT_ID,
                           client_secret=private.CLIENT_SECRET,
                           password=private.REDDIT_USER_PASSWORD,
                           user_agent=private.USER_AGENT,
                           username=private.REDDIT_USERNAME,
                           config_interpolation='basic',
                           requestor_class=None,
                           requestor_kwargs=None,
                           token_manager=None
                           )

subreddit_list = dict()
# for redditClient

# find all subreddits associated with the search terms in settings
for search_term in settings.SUBREDDITS:
    list_of_subs = redditClient.subreddits.search(search_term)  # get subreddits associated with that search term
    subreddit_list[search_term] = list_of_subs  # add the key : value pair search_term : subreddits[] to the subreddits dictionary

# save that array to a new dict subreddit_content with k:v being subreddit:array of submissions
subreddit_content = dict()
for sub in subreddit_list:  # go through subreddits dict, for each subreddit...
    submissions_list = []
    for submission in redditClient.subreddit(
            sub).new():  # get the top 100 newest submissions from the subreddit and save them to a list.
        submissions_list.append(submission)
    subreddit_content[
        sub.title()] = submissions_list  # save that list to a new dict subreddit_content with k:v being subreddit:array of submissions
    # the dict should now have all submissions from all subreddits searched.

post_comments = dict()
for submission in subreddit_content:
    comments = []  # list to hold all comments
    for comment in submission:  # go through every comment in the submission
        print(comment)
# ITERATE OVER EACH ONE AND PULL THE POSTS AND FORMAT AND STORE THEM AS YOU LOOP
