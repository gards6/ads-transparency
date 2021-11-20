import os
import json

os.chdir("/Users/JackGardner/Coding_Git/ads/")

with open('twitter_political_ads.txt', 'r') as file:
    data = file.read()

data = json.loads(data)
print(type(data))
print(data.keys())
# archives is a just a list format of all the data, and the elements of the list are dicts
"""
Example -- get a single tweet.
"""
# print(type(data["archives"][0]))
# # get the dict keys: dict_keys(['ads_account', 'tweets'])
# print(data["archives"][0].keys())
# # again, tweets is a list of dicts, and the keys to the dicts: dict_keys(['impressions', 'spend', 'ad_campaigns', 'reported_urls', 'tweet_text', 'tweet_url'])
# print(data["archives"][0]["tweets"][0].keys())
# # tweet_text is what we want
# print(data["archives"][0]["tweets"][0]["tweet_text"])

"""
Get all the tweets.
"""
from langdetect import detect

text_list = []
def parse_political(data):
    archives = data["archives"]
    for archive_dict in archives:
        tweets = archive_dict["tweets"]
        for tweet_dict in tweets:
            tweet_text = tweet_dict["tweet_text"]
            if detect(tweet_text) == "en":
                # Only include tweets encoded with ASCII, removes emojis and tweets in non latin alphabet
                tweet_text = tweet_text.strip().encode("ascii", "ignore").decode("ascii")
                tweet_text = tweet_text.replace("\n", " ")
                text_list.append(tweet_text)
            else:
                break

parse_political(data)

# 1689 tweets
# print(text_list)
print(len(text_list))
import pandas as pd
df = pd.DataFrame(text_list, columns = ["political_ad_tweets"])
df.to_csv("twitter_political_ad_tweets.csv")
