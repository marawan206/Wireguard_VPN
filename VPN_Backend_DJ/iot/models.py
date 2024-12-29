from django.db import models

# Create your models here.
class DeviceStatus(models.Model):
    # Device status can be a string, boolean, or any other data type,
    # but here we're keeping it simple with a CharField
    status = models.CharField(max_length=100, default="OFF")

    def __str__(self):
        return f"Device Status: {self.status}"