#!/usr/bin/python3.6

from twitter.stream import MyStreamListener,
from twitter.api import Twitter

def main(clube, output_path='./'):
    #instanciando API
    api = Twitter('cfg/config.cfg')

    myStreamListener = MyStreamListener(output_file='{}{}.csv'.format(output_path, clube))
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('Indique um clube!')
