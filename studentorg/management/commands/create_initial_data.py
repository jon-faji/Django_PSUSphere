from django.core.management.base import BaseCommand
from faker import Faker
import random
from studentorg.models import College, Program, Organization, Student, OrgMember


class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_colleges(5)
        self.create_programs(10)
        self.create_organization(5)
        self.create_students(20)
        self.create_memberships(20)
        self.stdout.write(self.style.SUCCESS('All initial data created successfully.'))

    def create_colleges(self, count):
        fake = Faker()
        for _ in range(count):
            College.objects.get_or_create(college_name=fake.company())
        self.stdout.write(self.style.SUCCESS('Colleges created successfully.'))

    def create_programs(self, count):
        fake = Faker()
        colleges = list(College.objects.all())
        if not colleges:
            self.stdout.write(self.style.WARNING("No colleges found!"))
            return
        for _ in range(count):
            Program.objects.get_or_create(
                prog_name=fake.bs(),
                college=random.choice(colleges)
            )
        self.stdout.write(self.style.SUCCESS('Programs created successfully.'))

    def create_organization(self, count):
        fake = Faker()
        colleges = list(College.objects.all())
        if not colleges:
            self.stdout.write(self.style.WARNING("No colleges found!"))
            return
        for _ in range(count):
            words = [fake.word() for _ in range(2)]
            Organization.objects.get_or_create(
                name=' '.join(words).title(),
                college=random.choice(colleges),
                description=fake.sentence()
            )
        self.stdout.write(self.style.SUCCESS('Organizations created successfully.'))

    def create_students(self, count):
        fake = Faker('en_PH')
        programs = list(Program.objects.all())
        if not programs:
            self.stdout.write(self.style.WARNING("No programs found!"))
            return
        for _ in range(count):
            Student.objects.create(
                student_id=f"{fake.random_int(2020, 2025)}-{fake.random_int(1, 8)}-{fake.random_number(digits=4)}",
                lastname=fake.last_name(),
                firstname=fake.first_name(),
                middlename=fake.last_name(),
                program=random.choice(programs)
            )
        self.stdout.write(self.style.SUCCESS('Students created successfully.'))

    def create_memberships(self, count):
        fake = Faker()
        students = list(Student.objects.all())
        organizations = list(Organization.objects.all())
        if not students or not organizations:
            self.stdout.write(self.style.WARNING("No students or organizations found!"))
            return
        for _ in range(count):
            OrgMember.objects.create(
                student=random.choice(students),
                organization=random.choice(organizations),
                date_joined=fake.date_between(start_date="-2y", end_date="today")
            )
        self.stdout.write(self.style.SUCCESS('Org memberships created successfully.'))