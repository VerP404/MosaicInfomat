from django.contrib import admin
from .models import Block, Button, Page, Settings


class ButtonInline(admin.TabularInline):
    model = Button
    extra = 1


class BlockAdmin(admin.ModelAdmin):
    inlines = [ButtonInline]


admin.site.register(Block, BlockAdmin)
admin.site.register(Page)
admin.site.register(Settings)
