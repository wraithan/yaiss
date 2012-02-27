from annoying.decorators import render_to
from writer.models import Nick, Channel, Line
from chartit import DataPool, Chart


@render_to('reader/full.html')
def full(request):
    nicks = Nick.objects.filter(ignore=False)
    channels = Channel.objects.filter(name__startswith='#')
    x_axis = '", "'.join(channels.values_list('name', flat=True))
    nick_count = ', '.join([unicode(channel.nick_count) for channel in channels])
    line_count = ', '.join([unicode(channel.line_count) for channel in channels])
    return {'nicks': nicks, 'x_axis': x_axis,
            'nick_count': nick_count, 'line_count': line_count}
