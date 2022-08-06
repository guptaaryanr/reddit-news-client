import praw
import pandas as pd

id = '_PoNf05jx82wXSw2wUZgHw'
secret = 'TQYRzyve4PcJWBiNo2Oauuwqeec1JA'
titles = []

reddit = praw.Reddit(client_id=id, client_secret=secret, user_agent='trends')

hot_posts = reddit.subreddit('politics').hot(limit=10)
for post in hot_posts:
    titles.append([post.title, post.score, post.num_comments, post.created])

titles = pd.DataFrame(titles, columns=['title', 'score', 'comments', 'created'])
titles.to_csv('trending.csv', index=False)
print(titles)