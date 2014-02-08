from django.http import HttpResponse
from django.template import Context, loader

def home(request):

    t = loader.get_template('home.html')
    c = Context({})
    
    return HttpResponse(t.render(c))
