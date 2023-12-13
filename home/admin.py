from django.contrib import admin
from .models import Contact, btech, mtechai, mscdf, mtechcs, pgd
from django.utils.html import format_html

# Register your models here.

admin.site.register(Contact)


# admin.site.register(btech)
# #admin.site.register(mtechai)
# admin.site.register(mtechcs)
# admin.site.register(mscdf)
# admin.site.register(pgd)

class MtechaiAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', 'email', 'dob', 'aadhar', 'gender', 'category', 'cgpa', 'gatescore', 'pincode',
                    'Photo', 'GATE', 'Category_Certificate', 'SIGN', 'Marksheet']


admin.site.register(mtechai, MtechaiAdmin)


class MtechcsAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', 'email', 'dob', 'aadhar', 'gender', 'category', 'cgpa', 'gatescore', 'pincode',
                    'Photo', 'GATE', 'Category_Certificate', 'SIGN', 'Marksheet']


admin.site.register(mtechcs, MtechcsAdmin)


class BtechAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', 'email', 'dob', 'aadhar', 'gender', 'category', 'percent', 'percentile',
                    'pincode', 'Photo', 'JEE', 'Category_Certificate', 'SIGN', 'Marksheet']


admin.site.register(btech, BtechAdmin)


class MSCDFAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', 'email', 'dob', 'aadhar', 'gender', 'category', 'cgpa', 'pincode', 'Photo',
                    'Category_Certificate', 'SIGN', 'Marksheet']


admin.site.register(mscdf, MSCDFAdmin)


class PGDAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', 'email', 'dob', 'aadhar', 'gender', 'category', 'cgpa', 'pincode', 'Photo',
                    'Category_Certificate', 'SIGN', 'Marksheet']


admin.site.register(pgd, PGDAdmin)
