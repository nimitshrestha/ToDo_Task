from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


# Create your models here.
class Task(models.Model):    
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    ]
    
    #Defined Fields of DataBaseTable
    task_id = models.AutoField(primary_key=True)
    task_title = models.CharField(max_length=100)
    task_description = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add = True)
    tags = models.CharField(max_length=255, blank=True, null=True)      #optional field
    due_date = models.DateField(null=True, blank=True)      #optional field
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OPEN')

    def __str__(self):
        return self.task_title
    
    
    #Validate Due_date cannot be before Timestamp
    def clean(self):
        if self.due_date is None:
            pass
        else:
            if self.due_date < timezone.now().date():
                raise ValidationError("Due Date cannot be before Timestamp created.")
            
    
    #Stores only unique Tags
    def save(self, *args, **kwargs):
        if self.tags:
            self.tags = ",".join(set(self.tags.split(",")))
        self.full_clean()   #check for validation of due_date
        super().save(*args, **kwargs)   #overridden instance save