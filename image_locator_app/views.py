from django.http import HttpResponse
from django.template import Context, loader

from image_locator_app.models import DroneImage

def home(request):

    t = loader.get_template('home.html')
    c = Context({'drone_images': DroneImage.objects.all() })
    
    return HttpResponse(t.render(c))
