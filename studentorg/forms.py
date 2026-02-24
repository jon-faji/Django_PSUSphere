from django import forms
from .models import College, Program, Organization, Student, OrgMember

# ------------------ College ------------------
class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = ['name', 'address']

# ------------------ Program ------------------
class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['name', 'college']

# ------------------ Organization ------------------
class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'college', 'description']

# ------------------ Student ------------------
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'program', 'college']

# ------------------ OrgMember ------------------
class OrgMemberForm(forms.ModelForm):
    class Meta:
        model = OrgMember
        fields = ['name', 'role', 'organization']