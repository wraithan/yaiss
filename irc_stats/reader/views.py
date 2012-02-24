from annoying.decorators import render_to
from writer.models import Nick

@render_to('reader/full.html')
def full(request):
    nicks = Nick.objects.all()
    return {'nicks': nicks}
