from django.contrib import admin

# Register your models here.
from adminmodule import models

admin.site.register(models.AdminRegister)
admin.site.register(models.User)
admin.site.register(models.Food)
admin.site.register(models.Income)
admin.site.register(models.Complaint)
admin.site.register(models.Notification)
admin.site.register(models.StaffRegister)
admin.site.register(models.HostelDetails)
admin.site.register(models.Payment)
admin.site.register(models.Attendance)