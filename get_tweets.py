import os
from searchtweets import ResultStream, gen_request_parameters, load_credentials

os.chdir("/Users/JackGardner/Coding_Git/ads/")

search_args = load_credentials("twitter_keys.yaml",
                                       yaml_key="search_tweets_v2",
                                       env_overwrite=False)
# Twitter API Query
query = gen_request_parameters("of lang:en -is:retweet",
                                tweet_fields = 'text,id',
                                results_per_call=10,
                                granularity = None)
# Obtain results
rs = ResultStream(request_parameters=query,
                    max_results=10,
                    max_pages=1,
                    **search_args)
results = list(rs.stream())
text_list = []
# Put the text of each Tweet into a list
for result in results:
    tweets = result['data']
    for tweet in tweets:
        tweet_text = tweet['text']
        tweet_text = tweet_text.strip().encode("ascii", "ignore").decode("ascii")
        tweet_text = tweet_text.replace("\n", " ")
        text_list.append(tweet_text)

import pandas as pd
df = pd.DataFrame(text_list, columns=['general_tweets'])
df.to_csv("twitter_general_tweets_v2.csv", mode = 'a', header = False)
