from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Organization, OrgMember, Student, College, Program
from .forms import (
    OrganizationForm,
    OrgMemberForm,
    StudentForm,
    CollegeForm,
    ProgramForm
)

""" Views for Organization model """

class OrgMemberListView(ListView):
    model = OrgMember
    template_name = "orgmember_list.html"
    context_object_name = "orgmembers"
    paginate_by = 5


class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = "orgmember_form.html"
    success_url = reverse_lazy("orgmember_list")


class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = "orgmember_form.html"
    success_url = reverse_lazy("orgmember_list")


class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = "orgmember_confirm_delete.html"
    success_url = reverse_lazy("orgmember_list")

""" Views for Student model """

class StudentListView(ListView):
    model = Student
    template_name = "student_list.html"
    context_object_name = "students"
    paginate_by = 5


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy("student_list")


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy("student_list")


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "student_confirm_delete.html"
    success_url = reverse_lazy("student_list")

""" Views for College model """

class CollegeListView(ListView):
    model = College
    template_name = "college_list.html"
    context_object_name = "colleges"
    paginate_by = 5


class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = "college_form.html"
    success_url = reverse_lazy("college_list")


class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = "college_form.html"
    success_url = reverse_lazy("college_list")


class CollegeDeleteView(DeleteView):
    model = College
    template_name = "college_confirm_delete.html"
    success_url = reverse_lazy("college_list")

""" Views for Program model """

class ProgramListView(ListView):
    model = Program
    template_name = "program_list.html"
    context_object_name = "programs"
    paginate_by = 5


class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = "program_form.html"
    success_url = reverse_lazy("program_list")


class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = "program_form.html"
    success_url = reverse_lazy("program_list")


class ProgramDeleteView(DeleteView):
    model = Program
    template_name = "program_confirm_delete.html"
    success_url = reverse_lazy("program_list")