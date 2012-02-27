from django.db import models
from writer import LINE_ACTION_TYPE_CHOICES

class Line(models.Model):
    """ A line of text in IRC """
    time = models.DateTimeField()
    message = models.TextField()
    nick = models.ForeignKey('writer.Nick')
    channel = models.ForeignKey('writer.Channel')
    action_type = models.IntegerField(choices=LINE_ACTION_TYPE_CHOICES)


class Nick(models.Model):
    """ A user who spoke or did an action. """
    name = models.CharField(max_length=255)
    server = models.ForeignKey('writer.Server')
    ignore = models.BooleanField(default=False)

    @property
    def first_seen(self):
        return self.line_set.all().order_by('time')[0].time

    @property
    def random_quote(self):
        return self.line_set.all().order_by('?')[0].message


class Channel(models.Model):
    """ A channel that an action happened in. """
    name = models.CharField(max_length=255)
    server = models.ForeignKey('writer.Server')

    @property
    def first_seen(self):
        return self.line_set.all().order_by('time')[0].time


class Server(models.Model):
    """ A server that an action happened on. """
    name = models.CharField(max_length=255)
