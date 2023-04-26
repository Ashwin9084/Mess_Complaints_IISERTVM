from django import forms
from .models import Hygiene_Complaint
from .models import Finance_Complaint
from .models import Menu_Complaint
from .models import Staff_Complaint
from .models import Icafe_Complaint

class Hygiene_ComplaintForms(forms.ModelForm):
    
    class Meta:
        model = Hygiene_Complaint
        fields = ['name', 'email', 'cdh', 'complaint']

class Finance_ComplaintForms(forms.ModelForm):
    
    class Meta:
        model = Finance_Complaint
        fields = ['name', 'email', 'complaint']
        
class Menu_ComplaintForms(forms.ModelForm):
    
    class Meta:
        model = Menu_Complaint
        fields = ['name', 'email', 'cdh', 'item', 'complaint']

class Staff_ComplaintForms(forms.ModelForm):
    
    class Meta:
        model = Staff_Complaint
        fields = ['name', 'email', 'cdh', 'complaint']

class Icafe_ComplaintForms(forms.ModelForm):
    
    class Meta:
        model = Icafe_Complaint
        fields = ['name', 'email', 'icafe', 'complaint']
