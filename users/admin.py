from django.contrib import admin

from users.models import Profile, Certificate, Skill

admin.site.register(Certificate)
admin.site.register(Skill)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('type', 'signup_confirmation')
