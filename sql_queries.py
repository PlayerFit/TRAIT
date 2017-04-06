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
list_of_favorites = "select favorite_count from tweet where user_id = {};" # FORMAT ARGS: player_id
list_of_retweets = "select retweet_count from tweet where user_id = {};" # FORMAT ARGS: player_id
num_retweets = "select count(*) from tweet where user_id = {} and retweet = True" # FORMAT ARGS: player_id
