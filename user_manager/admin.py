from django.contrib import admin

from user_manager.models import UserExtra, UserProfile, Experience, Resume


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_display.extend([field.name for field in UserProfile._meta.get_fields() if not field.is_relation])
    raw_id_fields = ['user']


class UserExtraAdmin(admin.ModelAdmin):
    list_display = ['userprofile']
    list_display.extend([field.name for field in UserExtra._meta.get_fields() if not field.is_relation])
    raw_id_fields = ['userprofile']


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['userprofile']
    list_display.extend([field.name for field in Experience._meta.get_fields() if not field.is_relation])
    raw_id_fields = ['userprofile']


class ResumeAdmin(admin.ModelAdmin):
    list_display = ['userprofile']
    list_display.extend([field.name for field in Resume._meta.get_fields() if not field.is_relation])
    raw_id_fields = ['userprofile']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserExtra, UserExtraAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Resume, ResumeAdmin)
