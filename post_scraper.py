from constants import private
import json
import praw
import logging
from RedditPost import RedditPost

# set up logging as advised per the praw documentation
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
for logger_name in ("praw", "prawcore"):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

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


# todo need to make a database service. need to make sure the json object is
#  coming out right in ths scrape subreddit func, need a class to iterate through
#  a list of subreddits and call scrape on each one and store the resulting lists
#  in the db with the database service

# the subreddit_path should be the url path element to the sub you want to scrape (/r wall street bets would be "wallstreetbets")
def scrape_subreddit(self, subreddit_path):
    list_of_posts = dict()
    subreddit_to_scrape = redditClient.subreddit(subreddit_path)
    # loop through top 100 new posts
    #todo remove limit in production,just for tests to be smaller
    for post in subreddit_to_scrape.new(limit=1):
        # save post text
        post_text = post.selftext
        # create a dict to hold the comments
        comments = dict()
        # we can get comments as a commentForest iterable object from submission object
        submission = redditClient.submission(post)
        # change comment sort order to sort by newest posts first
        submission.comment_sort = 'new'
        # replace_more method call ensures comment trees are complete
        # when a 'see more comments' button would have lead to more hidden comments
        submission.comments.replace_more()
        # get a flattened list of all comment trees
        # loop through the comments ...
        for comment in submission.comments.list():
            comments[comment.id] = comment.body     # and add them to the dictionary
        # create a post object with the post title, text, and a dictionary of all the comments
        # add it to the list of posts dictionary with the title as key
        list_of_posts[post.title] = json.dumps(RedditPost(post.title, post_text, comments))
        # return a dictionary with the format: post_title: RedditPost
    return list_of_posts
