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

# (Do not submit.) You can re-use the keys created in the previous part
# of the assignment but this program must be named tweet-a-pic.py. This
#program must be defined in its own virtual environment. This program
# takes two arguments. The first argument is a string which is the message
# portion of the tweet. The second argument is the path to an image which is
# going to be attached to the tweet. The program needs to post a status update
# to twitter which includes both the message and the image. Be aware that
# posting media lowers the character limit by 26 characters, maybe more.

import sys
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
	oauth_dance("little-tweet", CONSUMER_KEY, CONSUMER_SECRET, MY_TWITTER_CREDS)

oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)

# log in to Twitter
t = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

message = sys.argv[1] # "Uhh..."
image_path = sys.argv[2] # "lol.jpeg"

with open(sys.argv[2], "rb") as imagefile:
    params = {"media[]": imagefile.read(), "status": sys.argv[1]}

t.statuses.update_with_media(**params)