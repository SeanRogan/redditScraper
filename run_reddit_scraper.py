import constants.settings
from post_scraper import scrape_subreddit as scrape
import db_handler
# dict to store raw data before entering to the database
raw_dataset = dict()

# run_scrape calls the post scraper for all the subreddits in the list,
# and adds them all to the raw dataset and returns it
def run_scrape():
    for sub in constants.settings.SUBREDDITS:
        raw_dataset[sub] = scrape(sub)

    return raw_dataset

# store the dataset in the database
db_handler.store_in_database(run_scrape())
