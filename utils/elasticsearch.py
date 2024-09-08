from haystack.backends.elasticsearch7_backend import (
    Elasticsearch7SearchBackend, Elasticsearch7SearchEngine)


class CustomElasticsearchBackend(Elasticsearch7SearchBackend):
    def __init__(self, connection_alias, **connection_options):
        super().__init__(connection_alias, **connection_options)
        self.index_name_mapping = {
            'Post': 'haystack_post',
            'User': 'haystack_user',
        }

    def update(self, index, iterable, commit=True):
        model_name = index.get_model().__name__
        index_name = self.index_name_mapping.get(model_name, 'haystack')
        self.index_name = index_name
        super().update(index, iterable, commit)

    def clear(self, indexes=None, commit=True):
        if indexes:
            for index in indexes:
                model_name = index.get_model().__name__
                index_name = self.index_name_mapping.get(model_name,
                                                         'haystack')
                self.index_name = index_name
                super().clear([index], commit=commit)
        else:
            for model_name, index_name in self.index_name_mapping.items():
                self.index_name = index_name
                super().clear(commit=commit)

    def search(self, query_string, **kwargs):
        models = kwargs.get('models', [])
        if models:
            model_list = list(models)
            model_name = model_list[0].__name__
            index_name = self.index_name_mapping.get(
                model_name, 'haystack')
            self.index_name = index_name

        return super().search(query_string, **kwargs)


class CustomElasticsearchEngine(Elasticsearch7SearchEngine):
    backend = CustomElasticsearchBackend
