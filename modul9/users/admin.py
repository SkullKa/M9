from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import ProfileUser


# class ProfileUserAdmin(UserAdmin):
#     add_form = ProfileCreationForm
#     form = ProfileChangeForm
#     model = ProfileUser

    # list_display = ('username','email', 'name', 'surname', 'date_of_birth', 'gender')

admin.site.register(ProfileUser)
