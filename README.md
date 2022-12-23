# redditScraper
A service to webscrape reddit posts and add them to a database for later data analysis

## Pre-Requisites
The service is built with python 3.10, and uses a PostgreSQL database of the latest stable version.
It also requires several python packages as dependencies.
## Install
to install and use the service, first create a directory to clone the repository into
```
mkdir reddit_scraper_directory
```
navigate to the new directory you just created and clone the repo into it with 
```
cd reddit_scraper_directory
git clone https://github.com/SeanRogan/redditScraper
```
navigate to the constants folder with ```cd constants```
create a private.py file with ```touch private.py``` to store sensitive information. 
then use the ```pip install requirements.txt``` command to install required packages.

# Sensitive Information
this scraper requires several sensitive pieces of information to be use in the code. 
Your Client id and secret, username and password, and a database connection string 
with the username and password visible, are all potential vulnerabilities that shouldnt be hardcoded into the program. 
To keep things separate, the application calls these strings from a private.py file. the file should look like this:
```
# the following value are fake placeholders, make sure you replace them with your real API and DB credentials
USER_AGENT = "python:com.yourname.appname:v1.0(by /u/yourRedditUsername)"
CLIENT_ID = "_j2dfnef32h2ZCEMw"
CLIENT_SECRET = "_fddEB-1-YHLHloh3fFVDAVgdsSDV"
DB_CONNECTION_STRING = "postgresql://user:pass@dbprovider.cloudhost.com:5432/postgres"
REDDIT_USER_PASSWORD = "password"
REDDIT_USERNAME = "yourUserName"
```
# Reddit API Credentials
To use the scraper youll need to sign up for a reddit account here https://reddit.com , and create a reddit app here https://www.reddit.com/prefs/apps. Make sure you create a 'script' type application. Then save your credentials into the private.py file.
# Data Storage
The scraper is made to work with a postgresql database. If you have a database simply add your connection string in the private.py file. the database connection string format for postgresql is as follows:  
### postgresql://username:password@hostname:port/dbname 

# How to set up for your first scrape
  
# Happy Scraping 🎅🏻

