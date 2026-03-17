from django.contrib import admin
from django.urls import path, include
from studentorg.views import (
    HomePageView,
    OrganizationList,
    OrganizationCreateView,
    OrganizationUpdateView,
    OrganizationDeleteView,
    OrgMemberListView,
    OrgMemberCreateView,
    OrgMemberUpdateView,
    OrgMemberDeleteView,
    StudentListView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
    CollegeListView,
    CollegeCreateView,
    CollegeUpdateView,
    CollegeDeleteView,
    ProgramListView,
    ProgramCreateView,
    ProgramUpdateView,
    ProgramDeleteView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    # Home / Dashboard
    path('', HomePageView.as_view(), name='home'),

    # Organization URLs
    path('organizations/', OrganizationList.as_view(), name='organization_list'),
    path('organizations/add/', OrganizationCreateView.as_view(), name='organization-add'),
    path('organizations/<int:pk>/', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organizations/<int:pk>/delete/', OrganizationDeleteView.as_view(), name='organization-delete'),

    # OrgMember URLs
    path('orgmembers/', OrgMemberListView.as_view(), name='orgmember_list'),
    path('orgmembers/add/', OrgMemberCreateView.as_view(), name='orgmember-add'),
    path('orgmembers/<int:pk>/', OrgMemberUpdateView.as_view(), name='orgmember-update'),
    path('orgmembers/<int:pk>/delete/', OrgMemberDeleteView.as_view(), name='orgmember-delete'),

    # Student URLs
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/add/', StudentCreateView.as_view(), name='student-add'),
    path('students/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),

    # College URLs
    path('colleges/', CollegeListView.as_view(), name='college_list'),
    path('colleges/add/', CollegeCreateView.as_view(), name='college-add'),
    path('colleges/<int:pk>/', CollegeUpdateView.as_view(), name='college-update'),
    path('colleges/<int:pk>/delete/', CollegeDeleteView.as_view(), name='college-delete'),

    # Program URLs
    path('programs/', ProgramListView.as_view(), name='program_list'),
    path('programs/add/', ProgramCreateView.as_view(), name='program-add'),
    path('programs/<int:pk>/', ProgramUpdateView.as_view(), name='program-update'),
    path('programs/<int:pk>/delete/', ProgramDeleteView.as_view(), name='program-delete'),
]