import praw
import json
import sys
import requests

id = '_PoNf05jx82wXSw2wUZgHw'
secret = 'TQYRzyve4PcJWBiNo2Oauuwqeec1JA'
titles = []

reddit = praw.Reddit(client_id=id, client_secret=secret, user_agent='trends')

def alerts(message):
    #url = "https://hooks.slack.com/services/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"
    title = ("News")
    slack_data = {"username": "Test", "attachments": [{
        "color": "#B337ED",
        "fields": [{
            "title": title,
            "value": message,
            "short": "false",
        }]
    }]}

    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json",
    'Content-Length': byte_length}
    response = requests.post(url, data = json.dumps(slack_data), headers = headers)

    if response.status_code != 200:
        raise Exception(response.status_code, response.text)

# hot_posts = reddit.subreddit('politics').hot(limit=5)
# for post in hot_posts:
#     titles.append([post.title, post.score, post.num_comments, post.created])

# titles = pd.DataFrame(titles, columns=['title', 'score', 'comments', 'created'])
# titles.to_csv('trending.csv', index=False)
# print(titles)

if __name__ == '__main__':
    message = reddit.subreddit('politics').hot(limit=5)
    for msg in message:
        titles = (msg.url)
        alerts(titles)