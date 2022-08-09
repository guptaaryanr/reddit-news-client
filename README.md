# reddit-news-client

Used the praw library to get data from a reddit subreddit. trends.py is the file where I tried using and receiving information using this library and then sending using webhooks. But this required me to manually run the code every time I wanted something to be sent, which defeated the purpose.

I tried expanding this to send data using slash commands using WayScript (a sort of macros for coding type website) at first, which I didn't like as it was not a pure code approach, and then using the Slack RTM library, which did not work as Slack has now shifted to using granular permissions which messes with the library.

The way it finally worked was by setting up a Flask App, routing it to home page and then running the server on Repl for free. Took a bit of trial and error, as I was somewhat new to using it, but it finally works when I enter a slash command on the Slack channel and get a list of the top 5 posts on the r/politics subreddit.

Next steps are to expand it to cover the major types of subreddits I would want and then add more customizability to it. Hopefully, I can eventually find a way to make it work without having to manually create a new route for every single subreddit and modification I can think of. Maybe AI powered using the TensorFlow python library or the OpenCV python library? Or maybe a simpler way using string additions or something I'm overlooking right now?
