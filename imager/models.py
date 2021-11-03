from django.db import models

from uuid import uuid4


class Snippets(models.Model):
    id_snippet = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    code = models.TextField()
