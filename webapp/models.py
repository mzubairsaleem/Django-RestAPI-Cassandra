import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel


# Create your models here.
class products(DjangoCassandraModel):
    id = columns.UUID(primary_key=True)
    attributes = columns.Map(key_type=columns.Text, value_type=columns.Text)

    def __str__(self):
        return str(self.id)


class attributes(DjangoCassandraModel):
    __options__ = {'caching': {
        'keys': 'ALL',
        'rows_per_partition': 50000
    }}
    id = columns.UUID(primary_key=True)
    name = columns.Text(required=True)

    def __str__(self):
        return str(self.id)
