from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMember

# ------------------ College ------------------
@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']  
    search_fields = ['name', 'address']

# ------------------ Program ------------------
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'college']  
    list_filter = ['college']
    search_fields = ['name', 'college__name']

# ------------------ Organization ------------------
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'college', 'description']
    search_fields = ['name', 'college__name']

# ------------------ Student ------------------
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'program', 'college']
    search_fields = ['name', 'program__name', 'college__name']

# ------------------ OrgMember ------------------
@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'organization']
    search_fields = ['name', 'role', 'organization__name']