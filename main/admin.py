from django.contrib import admin
from .models import UserProfile,ContactProfile,Testimonial,Media,Portfolio,Blog,Certificate,Skill

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin): 
    list_display = ("id","user") 

class ContactAdmin(admin.ModelAdmin):
    list_display = ("id","timestamp","name")

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("id","name","is_active")

class MediaAdmin(admin.ModelAdmin):
    list_display = ("id","name")

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("id","name","is_active")
    readonly_fields = ("slug",)

class BlogAdmin(admin.ModelAdmin):
    list_display = ("id","name","is_active")
    readonly_fields = ("slug",)

class CertificateAdmin(admin.ModelAdmin):
    list_display = ("id","name")

class SkillAdmin(admin.ModelAdmin):
    list_display = ("id","name","score")

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(ContactProfile,ContactAdmin)
admin.site.register(Testimonial,TestimonialAdmin)
admin.site.register(Media,MediaAdmin)
admin.site.register(Portfolio,PortfolioAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Certificate,CertificateAdmin)
admin.site.register(Skill,SkillAdmin)
