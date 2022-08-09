from flask import Flask, request, Response
from threading import Thread
import slack_sdk as slack
import os
from pathlib import Path
from dotenv import load_dotenv
import praw

#Set the path of .env file using pathlib
token_path=Path('.') / '.env'
#loading env with load_dotenv function of python-dotenv module
load_dotenv(dotenv_path=token_path)
#saving bot api token as variable
bot_api_token = os.environ['bot_token']
reddit_id = os.environ['reddit_id']
reddit_secret = os.environ['reddit_secret']


reddit = praw.Reddit(client_id=reddit_id, client_secret=reddit_secret, user_agent='trends')

def subreddit(sub):
  message = reddit.subreddit(sub).hot(limit=5)
  return message

client=slack.WebClient(token=bot_api_token)

app = Flask('')

@app.route('/')
def home():
    return "The bot is alive"

@app.route('/news', methods=['POST'])
def news():
  data = request.form
  channel_id = data.get('channel_id')
  message = subreddit('politics')
  for msg in message:
    client.chat_postMessage(channel=channel_id, text="News", attachments=[{"pretext": msg.title, "text": msg.url}]
)
  return Response(), 200

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()