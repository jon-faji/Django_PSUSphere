from django.core.management.base import BaseCommand
from studentorg.models import College, Program, Student, Organization, OrgMember

class Command(BaseCommand):
    help = 'Seed the database with sample PSU data'

    def handle(self, *args, **kwargs):
        # Clear existing data (optional)
        College.objects.all().delete()
        Program.objects.all().delete()
        Student.objects.all().delete()
        Organization.objects.all().delete()
        OrgMember.objects.all().delete()

        # Colleges
        c1 = College.objects.create(name="College of Arts and Humanities", address="PSU Main Campus")
        c2 = College.objects.create(name="College of Business and Accountancy", address="PSU Main Campus")
        c3 = College.objects.create(name="College of Engineering Architecture and Technology", address="PSU Main Campus")
        c4 = College.objects.create(name="College of Sciences", address="PSU Main Campus")
        c5 = College.objects.create(name="College of Teacher Education", address="PSU Main Campus")

        # Programs
        p1 = Program.objects.create(name="Bachelor of Arts in Communication", college=c1)
        p2 = Program.objects.create(name="Bachelor of Science in Accountancy", college=c2)
        p3 = Program.objects.create(name="Bachelor of Science in Civil Engineering", college=c3)
        p4 = Program.objects.create(name="Bachelor of Science in Computer Science", college=c4)
        p5 = Program.objects.create(name="Bachelor of Elementary Education", college=c5)

        # Students
        s1 = Student.objects.create(name="Alice Mercado", program=p1, college=c1)
        s2 = Student.objects.create(name="Brian Santos", program=p2, college=c2)
        s3 = Student.objects.create(name="Cathy Reyes", program=p3, college=c3)
        s4 = Student.objects.create(name="David Cruz", program=p4, college=c4)
        s5 = Student.objects.create(name="Ella Dela Rosa", program=p5, college=c5)

        # Organizations
        org1 = Organization.objects.create(name="Arts Society", college=c1, description="Celebrating creativity and communication")
        org2 = Organization.objects.create(name="Business Leaders Club", college=c2, description="Future entrepreneurs unite")
        org3 = Organization.objects.create(name="Engineering Guild", college=c3, description="Innovators in tech and design")
        org4 = Organization.objects.create(name="Science Explorers", college=c4, description="Research and discovery club")
        org5 = Organization.objects.create(name="Education Advocates", college=c5, description="Teaching excellence group")

        # Org Members
        OrgMember.objects.create(name="Alice Mercado", role="President", organization=org1)
        OrgMember.objects.create(name="Brian Santos", role="Vice President", organization=org2)
        OrgMember.objects.create(name="Cathy Reyes", role="Secretary", organization=org3)
        OrgMember.objects.create(name="David Cruz", role="Treasurer", organization=org4)
        OrgMember.objects.create(name="Ella Dela Rosa", role="Member", organization=org5)

        self.stdout.write(self.style.SUCCESS("Sample PSU data created successfully."))