'''
- Scrap tweets using snscrap⭐ - https://betterprogramming.pub/how-to-scrape-tweets-with-snscrape-90124ed006af
- https://github.com/MartinBeckUT/TwitterScraper/blob/master/snscrape/cli-with-python/snscrape-python-cli.py
$ snscrape --jsonl --progress --max-results 100 twitter-search "from:elonmusk" > user-tweets.json
'''

# !pip install snscrape

import pandas as pd
import snscrape.modules.twitter as sntwitter

tweets = []
user_name = 'elonmusk'
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:{}'.format(user_name)).get_items()): 
    if i>50: 
        break
    tweets.append([tweet.date, tweet.id, tweet.content, tweet.user.username,
                        tweet.replyCount,tweet.retweetCount,tweet.likeCount,
                        tweet.quoteCount,tweet.lang,tweet.source,tweet.mentionedUsers]) 

df = pd.DataFrame(tweets, columns=['Datetime', 'Tweet Id', 'Text', 'Username',
                                        'replyCount','retweetCount','likeCount','quoteCount',
                                        'language','source','mentions'])


# using CLI
# import os
# os.system("snscrape --jsonl --max-results 10 twitter-search 'from:jack'> user-tweets.json")