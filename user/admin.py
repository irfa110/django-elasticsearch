from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import User
from haystack.query import SearchQuerySet


class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'phone_number', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Group Permissions', {'fields': ('groups', )}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'phone_number'),
        }),
    )
    search_fields = ['email', 'first_name', 'last_name',
                     'phone_number']
    ordering = ('-date_joined', )
    list_per_page = 25

    def get_search_results(self, request, queryset, search_term):
        if search_term:
            index = 1000
            sqs = SearchQuerySet().models(User).filter(
                content=search_term)[:index]
            ids = [result.pk for result in sqs]
            queryset = queryset.filter(pk__in=ids)
            return queryset, False
        return super().get_search_results(request, queryset, search_term)


admin.site.register(User, UserAdmin)
