from django.contrib import admin

from blog.models import Post, Category
from haystack.query import SearchQuerySet


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'is_active')
    raw_id_fields = ('category', )
    search_fields = ('title', 'content', 'user__email', 'user__phone_number')

    def get_search_results(self, request, queryset, search_term):
        if search_term:
            index = 1000
            # sqs = SearchQuerySet().models(Post).filter(
            #     content=search_term).order_by(
            #         '-date_joined')[:index]
            sqs = SearchQuerySet().models(Post).filter(
                content=search_term)[:index]
            ids = [result.pk for result in sqs]
            queryset = queryset.filter(pk__in=ids)
            return queryset, False
        return super().get_search_results(request, queryset, search_term)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
