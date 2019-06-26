from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Plane(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    built = models.DateTimeField()
    updated = models.DateTimeField(blank = 1, null = 1)

    def handle_built_and_updated(self):
        if self.built:
            self.updated = timezone.now()

        if not self.built:
            self.built = timezone.now()

    def __str__(self):
        if self.updated:
            return f"""{self.owner.username} has {self.name},
            built on {self.built}, updated on
            {self.updated}.
            """
        return f"""{self.owner.username} has {self.name}
        built on {self.built}.
        """