from django.db import models

# Create your models here.

class PublishStatus(models.TextChoices):
    PUBLISHED = 'publish', 'Published'
    COMING_SOON = 'soon', 'Coming Soon'
    DRAFT = 'draft', 'Draft'


class AccessRequirement(models.TextChoices):
    ANYONE = 'anyone', 'Anyone'
    EMAIL_REQUIRED = 'email', 'Email Required'

def handle_upload(instance,filename):
    return f"{filename}"

# course model 
class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=handle_upload,blank=True,null=True)
    access = models.CharField(max_length=10, choices=AccessRequirement.choices, default=AccessRequirement.ANYONE)
    status = models.CharField(max_length=10,choices=PublishStatus.choices,default=PublishStatus.DRAFT)

    @property 
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED