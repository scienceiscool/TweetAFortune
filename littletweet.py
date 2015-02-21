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

# (Do not submit.) Using the virtualenv program, create a virtual environment.
# Using pip, install the Python Twitter Tools. Next, register an application
# with Twitter at https://apps.twitter.com/app/new. This will give you the
# CONSUMER_KEY and the CONSUMER_SECRET strings needed to authenticate with the
# Twitter service. (The 'Name' field is the name of the program, 'Description'
# is a human understandable description of what the program does, 'Website' is
# your home page, leave 'Callback URL' blank. After you have accepted the terms
# and the keys are generated, click 'Permissions' and change the application from
# 'Read only' to 'Read and Write', then click 'Update Settings.' The keys will be
# regenerated after a few minutes. Use the new keys not the old keys. Finally,
# generate your 'Access Token' after the 'Read and Write' keys have been generated.
# KEEP THESE KEYS SECRET. Write a short program named littletweet.py that takes a
# string from the command line, verifies that it is shorter than 140 characters
# and then tweets it.

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

tweet = ''
tweet = sys.argv[1] # "I just wrote a program that tweets for me. What have you done?"

if len(tweet) < 140:
	t.statuses.update(status = tweet)