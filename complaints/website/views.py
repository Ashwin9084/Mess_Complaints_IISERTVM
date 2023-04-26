from django.shortcuts import render

from .forms import Hygiene_ComplaintForms
from .forms import Finance_ComplaintForms
from .forms import Menu_ComplaintForms
from .forms import Staff_ComplaintForms
from .forms import Icafe_ComplaintForms

from .models import Menu
from .models import CDH
from .models import Icafe

# Create your views here.
def home(request):
    all_items = Menu.objects.all
    all_cdh = CDH.objects.all
    all_icafe = Icafe.objects.all
    if request.method == 'POST':
        if 'hygiene' in request.POST:
            form = Hygiene_ComplaintForms(request.POST)
            if form.is_valid():
                form.save()
            return render(request, 'home.html', {'all_items': all_items, 'all_cdh': all_cdh, 'all_icafe': all_icafe})
        
        if 'finance' in request.POST:
            form = Finance_ComplaintForms(request.POST)
            if form.is_valid():
                form.save()
            return render(request, 'home.html', {'all_items': all_items, 'all_cdh': all_cdh, 'all_icafe': all_icafe})
        
        if 'menu' in request.POST:
            form = Menu_ComplaintForms(request.POST)
            if form.is_valid():
                form.save()
            return render(request, 'home.html', {'all_items': all_items, 'all_cdh': all_cdh, 'all_icafe': all_icafe})
        
        if 'staff' in request.POST:
            form = Staff_ComplaintForms(request.POST)
            if form.is_valid():
                form.save()
            return render(request, 'home.html', {'all_items': all_items, 'all_cdh': all_cdh, 'all_icafe': all_icafe})
        
        if 'icafe_btn' in request.POST:
            form = Icafe_ComplaintForms(request.POST)
            if form.is_valid():
                form.save()
            return render(request, 'home.html', {'all_items': all_items, 'all_cdh': all_cdh, 'all_icafe': all_icafe})
    
    else:
        return render(request, 'home.html', {'all_items': all_items, 'all_cdh': all_cdh, 'all_icafe': all_icafe})
