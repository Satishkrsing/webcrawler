from webcrawler.views import url_home
from django.contrib import admin
from webcrawler.models import Url_Monitor, Url_blacklist, Url_crawler_list, Url_crawler_other, Url_freejobalert, Url_home, Url_others, Url_sarkariresult, Url_pdf
# Register your models here.


class Url_order_free(admin.ModelAdmin):
    ordering = ('-timestamp',)


class Url_order_sar(admin.ModelAdmin):
    ordering = ('-timestamp',)


class Url_order_other(admin.ModelAdmin):
    ordering = ('-timestamp',)


class Url_order_pdf(admin.ModelAdmin):
    ordering = ('-timestamp',)

class Url_order_monitor(admin.ModelAdmin):
    ordering = ('-timestamp',)

admin.site.register(Url_sarkariresult, Url_order_free)
admin.site.register(Url_freejobalert, Url_order_sar)
admin.site.register(Url_others, Url_order_other)
admin.site.register(Url_pdf, Url_order_pdf)
admin.site.register(Url_home)
admin.site.register(Url_Monitor, Url_order_monitor)
admin.site.register(Url_blacklist)
admin.site.register(Url_crawler_list)
admin.site.register(Url_crawler_other)