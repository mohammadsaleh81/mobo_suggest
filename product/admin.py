from django.contrib import admin
from .models import Mobile, Gallery, Pictures


class PicturesInlineAdmin(admin.TabularInline):
    model = Pictures
    extra = 0


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
    inlines = [PicturesInlineAdmin]


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Mobile)
