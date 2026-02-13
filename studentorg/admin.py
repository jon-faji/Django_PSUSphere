from django.contrib import admin
from .models import College, Program, Organization

# -------------------------------
# Task A – CollegeAdmin
# -------------------------------
@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ("college_name", "created_at", "updated_at")  # show these columns
    search_fields = ("college_name",)  # add search by college_name
    list_filter = ("created_at",)  # filter by created_at

# -------------------------------
# Task B – ProgramAdmin
# -------------------------------
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("prog_name", "college")  # show program name and related college
    search_fields = ("prog_name", "college__college_name")  # search by program name or college name
    list_filter = ("college",)  # filter by college

# -------------------------------
# Task C – OrganizationAdmin
# -------------------------------
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "college", "description")  # show name, college, description
    search_fields = ("name", "description")  # search by name or description
    list_filter = ("college",)  # filter by college