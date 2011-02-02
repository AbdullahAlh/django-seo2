#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from rollyourown.seo.admin import register_seo_admin, get_inline
from django.contrib import admin
from userapp.seo import Coverage, WithSites

register_seo_admin(admin.site, Coverage)
register_seo_admin(admin.site, WithSites)

from userapp.models import Product, Page, Category, Tag, NoPath

class WithMetadataAdmin(admin.ModelAdmin):
    inlines = [get_inline(Coverage), get_inline(WithSites)]

admin.site.register(Product, admin.ModelAdmin)
admin.site.register(Page, admin.ModelAdmin)
admin.site.register(Tag, WithMetadataAdmin)
admin.site.register(NoPath, WithMetadataAdmin)

alternative_site = admin.AdminSite()

#from rollyourown.seo.admin import auto_register_inlines

alternative_site.register(Tag)
#auto_register_inlines(Coverage, alternative_site)
alternative_site.register(Page)
