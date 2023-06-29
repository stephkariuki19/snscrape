# import snscrape.modules.twitter as sntwitter
#https://medium.com/dataseries/how-to-scrape-millions-of-tweets-using-snscrape-195ee3594721
#(for all)
#https://github.com/JustAnotherArchivist/snscrape/blob/master/snscrape/modules/facebook.py
import pandas as pd
import snscrape

# importing libraries and packages
import snscrape.modules.twitter as sntwitter
import pandas



# Creating list to append tweet data
tweets_list1 = []


# Using TwitterSearchScraper to scrape data and append tweets to list
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:WHOKenya').get_items()):  # declare a username
    if i > 10:  # number of tweets you want to scrape
        break
    tweets_list1.append(
        [tweet.date, tweet.id, tweet.rawContent, tweet.user.username])  # declare the attributes to be returned

# Creating a dataframe from the tweets list above
tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
tweets_df1.to_json('response.json',indent=4)
print(tweets_df1)



