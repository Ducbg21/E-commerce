from django.db import models
from datetime import datetime
import os

def _upload_to(instance, filename):
    app_label = instance._meta.app_label
    model_name = instance.__class__.__name__
    date_path = datetime.today().strftime("%Y/%m/%d")
    upload_path = os.path.join(app_label, model_name, date_path, filename)
    return upload_path


class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_img = models.ImageField(upload_to=_upload_to, null=True, blank=True)

    def __str__(self):
        return self.name
