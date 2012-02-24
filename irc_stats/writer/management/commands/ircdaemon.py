from json import loads
from datetime import datetime

from django.core.management.base import BaseCommand
from redis import StrictRedis

from writer.models import Line, Nick, Channel, Server
from writer import LINE_ACTION_TYPE_MESSAGE

class Command(BaseCommand):
    args = ''
    help = 'The daemon to run along side the stats viewer.'

    def handle(self, *args, **options):
        self.redis = StrictRedis(host='localhost', port=6379, db=0).pubsub()
        self.redis.subscribe('in')
        for msg in self.redis.listen():
            message = loads(msg['data'])
            if message['version'] == 1:
                if message['type'] == 'privmsg':
                    Line.objects.create(time=datetime.now(),
                                        message=message['data']['message'],
                                        nick=Nick.objects.get_or_create(name=message['data']['sender'], server=Server.objects.get_or_create(name='irc.freenode.net')[0])[0],
                                        channel=Channel.objects.get_or_create(name=message['data']['channel'], server=Server.objects.get_or_create(name='irc.freenode.net')[0])[0],
                                        action_type=LINE_ACTION_TYPE_MESSAGE,)