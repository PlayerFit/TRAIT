from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

#Create a DBAPI connection
engine = create_engine("postgres://alhqpbkb:WQ-RjLbw5LrkrBMJcFKWWfbaxhsyReTs@babar.elephantsql.com:5432/alhqpbkb")

#Declare an instance of the Base class for mapping tables
Base = declarative_base()

# The Trait Model should be populated with anything we think
# we may use when running the classification. Write functions to
# get these values from the DB in trait.py
class Trait(Base):

    __tablename__ = 'trait'
    uid = Column(Text, ForeignKey('player.id'), primary_key=True)
    tweet_count = Column(BigInteger, nullable=False)
    average_favorites = Column(BigInteger, nullable=False)
    perc_tweets_morning = Column(Float, nullable=False)
    perc_tweets_afternoon = Column(Float, nullable=False)
    perc_tweets_evening = Column(Float, nullable=False)
    perc_tweets_after_midnight = Column(Float, nullable=False)
    perc_tweets_with_profanity = Column(Float, nullable=False)
    overall_tweet_sentiment = Column(Float, nullable=False)
    personal_desc_sentiment = Column(Float, nullable=False)
    num_followers = Column(BigInteger, nullable=False)
    retweet_count = Column(BigInteger, nullable=False)

    def __init__(self, uid, tweet_count, average_favorites, perc_tweets_morning,
                 perc_tweets_afternoon, perc_tweets_evening, perc_tweets_after_midnight,
                 perc_tweets_with_profanity, overall_tweet_sentiment, personal_desc_sentiment,
                 num_followers, retweet_count):
        self.uid = uid
        self.tweet_count = tweet_count
        self.average_favorites = average_favorites
        self.perc_tweets_morning = perc_tweets_morning
        self.perc_tweets_afternoon = perc_tweets_afternoon
        self.perc_tweets_evening = perc_tweets_evening
        self.perc_tweets_after_midnight = perc_tweets_after_midnight
        self.perc_tweets_with_profanity = perc_tweets_with_profanity
        self.overall_tweet_sentiment = overall_tweet_sentiment
        self.personal_desc_sentiment = personal_desc_sentiment
        self.num_followers = num_followers
        self.retweet_count = retweet_count

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
