# CS223P - Python Programming

# Author Name: Kathy Saad
# Project Title: Project 7 - RDB, Python Virtual Environments, PyPi, pip
# Project Status: Working
# External resources:
#	Class notes and handouts
#	https://www.snipplr.com/view/49167/
#	https://www.pypi.python.org/pypi/twitter/1.10.0/
#	https://www.pypi.python.org/pypi/twitter/1.15.0/
#	https://www.python.org/

import sqlite3
import sys
import random
import os
import twitter
from twitter import Twitter, OAuth, oauth_dance, write_token_file, read_token_file

CONSUMER_KEY = '<CONSUMER_KEY>'
CONSUMER_SECRET = '<CONSUMER_SECRET>'

oauth_token = '<oauth_token>'
oauth_secret = '<oauth_secret>'

# get twitter account login info
MY_TWITTER_CREDS = os.path.expanduser('~/.twitter_oauth.')
if not os.path.exists(MY_TWITTER_CREDS):
	oauth_dance("tweet-a-random-fortune-and-pic", CONSUMER_KEY, CONSUMER_SECRET, MY_TWITTER_CREDS)

oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)

# log in to Twitter
t = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

db = sys.argv[1]
conn = sqlite3.connect(db)
c = conn.cursor()

random_number = random.randint(1, 14334)
fortune = c.execute('select aphorism from fortunes where id=' + str(random_number) + ';').fetchone()[0]

if len(fortune) < 140:
	#random.choice(os.listdir("/home/kat/Desktop/tweetafortune/images/"))
	random_image_name = random.randint(1, 6)
	random_image_name = str(random_image_name) + '.jpg'

	with open(random_image_name, "rb") as imagefile:
		params = {"media[]": imagefile.read(), "status": fortune}

	t.statuses.update_with_media(**params)
else:
	while not(len(fortune) < 140):
		random_number = random.randint(1, 14334)
		fortune = c.execute('select aphorism from fortunes where id=' + random_number + ';').fetchone()[0]

	if len(fortune) < 140:
		random_image_name = random.randint(1, 6)
		random_image_name = str(random_image_name) + '.jpg'

		with open(random_image_name, "rb") as imagefile:
			params = {"media[]": imagefile.read(), "status": fortune}

		t.statuses.update_with_media(**params)

conn.close()