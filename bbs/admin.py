from django.contrib import admin
from .models import Topic,Trend

class TrendAdmin(admin.ModelAdmin):

    list_display    = ["word","dt","count"]


admin.site.register(Topic)
admin.site.register(Trend,TrendAdmin)

