from django.db import models
from django.db.models.fields import AutoFieldMixin, PositiveIntegerRelDbTypeMixin

class TinyIntegerField(models.IntegerField):
    description = "Tiny integer"

    def get_internal_type(self):
        return 'TinyIntegerField'

class PositiveTinyIntegerField(PositiveIntegerRelDbTypeMixin, TinyIntegerField):
    description = "Positive tiny integer"

    def get_internal_type(self):
        return 'PositiveTinyIntegerField'

    def formfield(self, **kwargs):
        return super().formfield(**{
            'min_value': 0,
            **kwargs,
        })

class TinyAutoField(AutoFieldMixin, TinyIntegerField):

    def get_internal_type(self):
        return 'TinyAutoField'

    def rel_db_type(self, connection):
        return TinyIntegerField().db_type(connection=connection)