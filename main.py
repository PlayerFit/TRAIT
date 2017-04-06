import sql_queries
from model import session
from tqdm import *
from sqlalchemy.exc import SQLAlchemyError

def main(argv):
    player_ids = session.query(Player).all()

    for id in tqdm(ids, "Player"):
        build_trait(id)
    commit()

def build_trait(player):
    t = Trait(
        uid = player.id
        tweet_count = player.tweet_count
        followers = player.follower_count
        verified = player.verified
        perc_retweets = execute_query([num_retweets, player.id]) / float(player.tweet_count)
        #TODO add/pick the rest of the fields
    )
    session.merge(t)

def commit():
    try:
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print (str(e))

if __name__ == "__main__":
    main(sys.argv[1:])
