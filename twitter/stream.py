import tweepy
import sys
import pytz as timezone
from datetime import timedelta
#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def __init__(self, output_file=sys.stdout):
        super(MyStreamListener,self).__init__()
        self.output_file = output_file

    def on_status(self, status):
        with open(self.output_file, 'a') as f:
            if not status.text.startswith('RT'):
                f.write('¬{}¬,¬{}¬\n'.format(status.created_at - timedelta(hours=3), status.text))

    def on_error(self, status_code):
        print(status_code)
        return False
