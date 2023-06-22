from django.contrib import admin
from home.models import Task

# Register your models here.

#Django-Admin Site 
class TaskAdmin(admin.ModelAdmin):
    #these elements display in tasks
    list_display = ['task_id', 'task_title', 'task_description', 'time', 'due_date', 'tags', 'status']
    list_filter = ['time', 'status']    # set filters for result of task
    search_fields = ['time', 'status']  # search field 

    #Add new Task from Admin-Site
    fieldsets = [
        ('About Task', {'fields': ['task_title', 'task_description','tags']}),
        ('Task Details', {'fields': ['status', 'due_date']}),
    ]

#model Registering
admin.site.register(Task, TaskAdmin)
