from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import redirect, render_to_response

from image_locator_app.models import DroneImage
from image_locator_app.forms import DroneImageForm

def landing(request):
    return render_to_response('landing.html')

def home(request):

    if request.method == 'POST':

        form = DroneImageForm(request.POST)

        if form.is_valid():
            image_object = DroneImage.objects.get(pk = request.POST.get("id"))
            image_object.water = request.POST.get("water", False)
            image_object.food = request.POST.get("food", False)
            image_object.shelter = request.POST.get("shelter", False)
            image_object.medicine = request.POST.get("medicine", False)
            image_object.protection = request.POST.get("protection", False)
            image_object.save()

        else:
            print 'The form is not valid' #for debugging purposes only. Remove later

        id = image_object.id + 1
    else:
        id = 1
    try:
        image_object = DroneImage.objects.get(pk=id)
        form = DroneImageForm(instance=image_object)
    except:
        return redirect('/')

    return render_to_response('home.html', {'random_image': image_object, 'form': form }, context_instance = RequestContext(request))
