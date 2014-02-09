from image_locator_app.models import DroneImage
from django.forms import ModelForm, TextInput

class DroneImageForm(ModelForm):
    class Meta:
        model = DroneImage
        fields = ['water', 'sanitation', 'food', 'shelter', 'medicine', 'protection', 'obstruction', 'comment']
        
