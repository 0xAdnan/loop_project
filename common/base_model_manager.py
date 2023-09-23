from django.db import models


class BaseManager(models.Manager):
    def create_object(self, **kwargs):
        obj = self.model(**kwargs)
        obj.save()
        return obj

    def update_object(self, obj, **kwargs):
        for attr, value in kwargs.items():
            setattr(obj, attr, value)
        obj.save()
        return obj

    def delete_object(self, obj):
        obj.delete()

    def filter_objects(self, **kwargs):
        return self.filter(**kwargs)

    # album = Album.objects.filter_objects(artist='The Beatles', release_date__year=1969).first()

