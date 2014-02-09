from image_locator_app.models import DroneImage
from django.forms import ModelForm, TextInput

class DroneImageForm(ModelForm):
    class Meta:
        model = DroneImage
        fields = ['status', 'interest_type', 'comment',]
        
