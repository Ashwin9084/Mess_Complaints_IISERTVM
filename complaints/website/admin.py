from django.contrib import admin
from .models import Menu
from .models import CDH
from .models import Icafe
from .models import Hygiene_Complaint
from .models import Finance_Complaint
from .models import Menu_Complaint
from .models import Staff_Complaint
from .models import Icafe_Complaint
# Register your models here.

admin.site.register(Menu)
admin.site.register(CDH)
admin.site.register(Icafe)
admin.site.register(Hygiene_Complaint)
admin.site.register(Finance_Complaint)
admin.site.register(Menu_Complaint)
admin.site.register(Staff_Complaint)
admin.site.register(Icafe_Complaint)
