from django.contrib import admin
from .models import Student,SilverToken,GoldToken,Menu,Feedback,NotEatingToday
# Register your models here.

admin.site.register(Student)
admin.site.register(SilverToken)
admin.site.register(GoldToken)
admin.site.register(Menu)
admin.site.register(Feedback)
# admin.site.register(Food)
admin.site.register(NotEatingToday)

