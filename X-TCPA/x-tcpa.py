import os
import sys
import tweepy
import platform
import optparse
from optparse import OptionParser
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from sys import platform as osid

## X-TCPA  -  X - Twitter Crawler (Python Application)  -  Als = Nemesis 2 ##

if osid == 'win32':
    print "I cannot run on windows...Maybe...But modifications have to be made..."
    print("")
    os.system("pause")
    sys.exit(1)

## Variables ##
plus = "\033[32m[+]\033[30m"
minus = "\033[31m[-]\033[30m"
info = "[I]"
regular = "[*]"

__version__ = '1.0.0'
xver = 1.0

if xver - .0 != __version__:
    print regular + " Using older version: ", xver
    pass  

## Consumer Key ##
consumer_key = '[ CONSUMER_KEY ]'
consumer_secret = '[ CONSUMER_SECRET ]'
access_token = '[ ACCESS_TOKEN ]'
access_secret = '[ ACCESS_SECRET ]'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

## Api ##
api = tweepy.API(auth)

def proc_or_store(tweet):
    print(json.dumps(tweet))

## Class streamer ##
class listener(StreamListener):
    def x_data(self, data):
        try:
            with open('python.json', 'a') as file3:
                file3.write(data)
                return True
        except BaseException as x_base_e:
            print("Error x_data: %s" % str(x_base_e))
            return True
    def x_error(self, status):
        print status
        return True


## Opts ##
if __name__ == '__main__':
    parser = OptionParser(usage="x-tcpa [OPTIONS] [ARGS]", conflict_handler="resolve")
    parser.add_option("-T", "--test", dest="test_program", default="False", help="Test program on home twitter account timeline.")
    parser.add_option("-L", "--listfriends", dest="list_friends", default="False", help="List all friends (followers) from your API.")
    parser.add_option("-J", "--jsonstore", dest="json_store", default="False", help="Store the API timeline as json.")
    parser.add_option("-t", "--tweetlist", dest="tweet_list", default="False", help="Display the list of all tweets.")
    parser.add_option("-A", "--tweet1perline", dest="tweet_1_per_line", default="False", help="Display tweets one per line.")
    parser.add_option("-l", "--tweetstream", dest="tweet_stream", default="False", help="Keep the connection alive, and gather everything.")
    parser.add_option("-V", "--version", dest="version", default="False", help="Display program version.")

    (options, args) = parser.parse_args()
    if len(args) != 1:
        print parser.error("Must give at least one argument\n")
        print parser.usage()
    if options.test_program == '1':
        for status in tweepy.Cursor(api.home_timeline).items(10):
            print plus + " Testing program (Home Page [ API ])\n"
            print(status.text)
    elif options.json_store == '1':
        for status in tweepy.Cursor(api.home_timeline).items(10):
            print plus + " Processing and Storing JSON\n"
            process or store(status. json)
    elif options.list_friends == '1':
        for firend in tweepy.Cursor(api.friends).items():
            process or store(friend. json)
    elif options.tweet_list == '1':
        print plus + " Gathering all Tweets\n"
        for tweet in tweepy.Cursor(api.user_timeline).items():
            process or store(tweet. json)
    elif options.tweet_1_per_line == '1':
        print plus + " Printing tweets 1 per line\n"
        proc_or_store()
    elif options.tweetstream == '1':
        search_term = raw_input("Enter the search term: ")
        if search_term == 'help':
            print info + " Try #'term'"
            pass
        twitter_stream = Stream(auth, listener())
        twitter_stream.filter(track=[search_term])
    elif options.version == 'show':
        print("")
        print "App version: ", __version__
        print("")
    else:
        print minus + " Unknown option..."
        pass
