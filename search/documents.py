from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from post.models import Post
from account.models import Account

@registry.register_document
class PostDocument(Document):
    author = fields.ObjectField(properties={
        'username': fields.TextField(),
    })

    retweeted_from = fields.ObjectField(properties={
        'username': fields.TextField(),
    })

    retweeted_by = fields.ObjectField(properties={
        'username': fields.TextField(),
    })

    class Index:
        name = 'posts'

    class Django:
        model = Post
        fields = {
            'body',
            'image',
            'video',
            'is_retweeted',
            'created_time',
        }
