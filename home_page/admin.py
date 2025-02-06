from django.contrib import admin
from home_page.models import Gig

admin.site.register(Gig)


admin.site.site_header = 'R1SE administration'

admin.site.site_title = 'Admin | R1SE'