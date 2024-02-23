from django.contrib import admin
from .models import User, Teacher, Student, Group, Email


admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Email)
