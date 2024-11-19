from django.contrib import admin
from .models import *


class aboutAdmin(admin.ModelAdmin):
    list_display = ("id", "img")


class projectHomeAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "h", "p", "link")


class projectAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "h", "p", "link")


class cvAdmin(admin.ModelAdmin):
    list_display = ("id", "pdf")


class contactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "phoneNumber", "message")


admin.site.register(about, aboutAdmin)
admin.site.register(projectHome, projectHomeAdmin)
admin.site.register(project, projectAdmin)
admin.site.register(cv, cvAdmin)
admin.site.register(contact, contactAdmin)
