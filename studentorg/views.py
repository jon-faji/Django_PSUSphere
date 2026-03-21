from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import College, Program, Organization, OrgMember, Student

# ---------------- Home Page ----------------
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Count objects
        context['college_count'] = College.objects.count()
        context['program_count'] = Program.objects.count()
        context['organization_count'] = Organization.objects.count()
        context['student_count'] = Student.objects.count()
        return context

# ---------------- College ----------------
class CollegeListView(ListView):
    model = College
    template_name = 'college_list.html'
    context_object_name = 'colleges'

class CollegeCreateView(CreateView):
    model = College
    fields = ['name', 'address']
    template_name = 'college_form.html'
    success_url = reverse_lazy('college_list')

class CollegeUpdateView(UpdateView):
    model = College
    fields = ['name', 'address']
    template_name = 'college_form.html'
    success_url = reverse_lazy('college_list')

class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'college_confirm_delete.html'
    success_url = reverse_lazy('college_list')

# ---------------- Program ----------------
class ProgramListView(ListView):
    model = Program
    template_name = 'program_list.html'
    context_object_name = 'programs'

class ProgramCreateView(CreateView):
    model = Program
    fields = ['name', 'college']
    template_name = 'program_form.html'
    success_url = reverse_lazy('program_list')

class ProgramUpdateView(UpdateView):
    model = Program
    fields = ['name', 'college']
    template_name = 'program_form.html'
    success_url = reverse_lazy('program_list')

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program_confirm_delete.html'
    success_url = reverse_lazy('program_list')

# ---------------- Student ----------------
class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'college', 'program']
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'college', 'program']
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('student_list')

# ---------------- Organization ----------------
class OrganizationList(ListView):
    model = Organization
    template_name = 'org_list.html'  
    context_object_name = 'organizations'

class OrganizationCreateView(CreateView):
    model = Organization
    fields = ['name', 'college', 'description']
    template_name = 'org_form.html'   
    success_url = reverse_lazy('organization_list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    fields = ['name', 'college', 'description']
    template_name = 'org_form.html'   
    success_url = reverse_lazy('organization_list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'    
    success_url = reverse_lazy('organization_list')

# ---------------- OrgMember ----------------
class OrgMemberListView(ListView):
    model = OrgMember
    template_name = 'orgmember_list.html'
    context_object_name = 'orgmembers'

class OrgMemberCreateView(CreateView):
    model = OrgMember
    fields = ['name', 'role', 'organization']
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy('orgmember_list')

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    fields = ['name', 'role', 'organization']
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy('orgmember_list')

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'orgmember_confirm_delete.html'
    success_url = reverse_lazy('orgmember_list')