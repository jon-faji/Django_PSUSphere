from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import College, Program, Organization, Student, OrgMember
from .forms import CollegeForm, ProgramForm, OrganizationForm, StudentForm, OrgMemberForm

# ------------------ Home ------------------
class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Dashboard counts
        context["college_count"] = College.objects.count()
        context["program_count"] = Program.objects.count()
        context["organization_count"] = Organization.objects.count()
        context["student_count"] = Student.objects.count()
        context["orgmember_count"] = OrgMember.objects.count()
        return context

# ------------------ College ------------------
class CollegeListView(ListView):
    model = College
    template_name = "college_list.html"
    context_object_name = "colleges"
    paginate_by = 5

    # Search feature
    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(name__icontains=query)
        return qs

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

# ------------------ Program ------------------
class ProgramListView(ListView):
    model = Program
    template_name = "program_list.html"
    context_object_name = "programs"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(college__name__icontains=query)
            )
        # Sorting
        allowed_sort = ["name", "college__name"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed_sort:
            qs = qs.order_by(sort_by)
        else:
            qs = qs.order_by("name")
        return qs

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

# ------------------ Student ------------------
class StudentListView(ListView):
    model = Student
    template_name = "student_list.html"
    context_object_name = "students"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)
            )
        return qs

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

# ------------------ OrgMember ------------------
class OrgMemberListView(ListView):
    model = OrgMember
    template_name = "orgmember_list.html"
    context_object_name = "orgmembers"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(organization__name__icontains=query) |
                Q(role__icontains=query)
            )

        # Sorting
        allowed_sort = ["name", "date_joined"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed_sort:
            qs = qs.order_by(sort_by)
        else:
            qs = qs.order_by("name")  
        return qs

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

# ------------------ Organization ------------------
class OrganizationList(ListView):
    model = Organization
    template_name = "org_list.html"
    context_object_name = "organizations"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )

        # Sorting
        allowed_sort = ["name", "college__name"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed_sort:
            qs = qs.order_by(sort_by)
        else:
            qs = qs.order_by("name")
        return qs

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_form.html"
    success_url = reverse_lazy("organization_list")

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_form.html"
    success_url = reverse_lazy("organization_list")

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = "org_del.html"
    success_url = reverse_lazy("organization_list")