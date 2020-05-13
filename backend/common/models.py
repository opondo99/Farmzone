# pylint: skip-file

import uuid

from django.db import models
from django.utils import timezone


class AbstractBase(models.Model):
    # pylint: disable=missing-docstring
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True)
    created = models.DateTimeField(db_index=True, default=timezone.now)
    created_by = models.UUIDField(null=True, blank=True)
    updated = models.DateTimeField(db_index=True, default=timezone.now)
    updated_by = models.UUIDField(null=True, blank=True)

    def preserve_created_and_created_by(self):
        """Preserve created and created_by during updates."""
        try:
            original = self.__class__.objects.get(pk=self.pk)
            self.created = original.created
            self.created_by = original.created_by
        except self.__class__.DoesNotExist:
            pass

    def save(self, *args, **kwargs):
        """Ensure validations are run and updated/created preserved."""
        self.updated = timezone.now()
        self.full_clean(exclude=None)
        self.preserve_created_and_created_by()
        super(AbstractBase, self).save(*args, **kwargs)

    class Meta:  # pylint: disable=D203
        """Define a default least recently used ordering."""

        abstract = True
        ordering = ('-updated', '-created')
