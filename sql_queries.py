from model import Trait, session

# executes given query with params
# returns the value
def execute_query(*args):
    return session.execute(build_query(args)).one_or_none()

# builds a query with query (arg[0]) and parameters (args[1:])
def build_query(*args):
    return args[0].format(tuple(args[1:]))

list_of_times = *** #(list) list of tweet times adjusted by UTC offset
num_deleted_tweets = *** #(int) total number of deleted tweets DONT KNOW IF POSSIBLE
location_on = *** #(int) number of tweets with location tracking on
list_of_favorites = "select favorite_count from tweet where user_id = {};".format(player_id) #(list) list of number of favorites per tweet
list_of_retweets = "select retweet_count from tweet where user_id = {};".format(player_id) #(list) list of number of retweets per tweet
num_retweets = *** #(int) number of times player has retweeted anything DONT KNOW IF POSSIBLE
