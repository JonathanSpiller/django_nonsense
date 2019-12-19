from django.contrib import admin
from .models import Person, Personality

class PersonAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name']

admin.site.register(Person, PersonAdmin)


class PersonalityAdmin(admin.ModelAdmin):
    list_display = ['id', 'happiness', 'introvert','mbti']

admin.site.register(Personality, PersonalityAdmin)

