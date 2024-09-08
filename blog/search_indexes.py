from haystack import indexes
from blog.models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    content = indexes.CharField(model_attr='content')
    user_id = indexes.IntegerField(null=True)
    user__email = indexes.CharField(null=True)
    user__phone_number = indexes.CharField(null=True)
    created_at = indexes.DateTimeField(model_attr='created_at')

    model_type = indexes.CharField()

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

    def prepare_model_type(self, obj):
        return 'post'

    def prepare_user__id(self, obj):
        user = obj.user._wrapped if hasattr(obj.user, '_wrapped') else obj.user
        return user.id if user else None

    def prepare_user__email(self, obj):
        user = obj.user._wrapped if hasattr(obj.user, '_wrapped') else obj.user
        return user.email if user else ""

    def prepare_user__phone_number(self, obj):
        user = obj.user._wrapped if hasattr(obj.user, '_wrapped') else obj.user
        return str(user.phone_number) if user else ""
