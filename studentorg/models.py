from django.db import models

# ------------------ College ------------------
class College(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name

# ------------------ Program ------------------
class Program(models.Model):
    name = models.CharField(max_length=255)
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name="programs")

    def __str__(self):
        return self.name

# ------------------ Student ------------------
class Student(models.Model):
    name = models.CharField(max_length=255)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="students")
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name="students")

    def __str__(self):
        return self.name

# ------------------ Organization ------------------
class Organization(models.Model):
    name = models.CharField(max_length=255)
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name="organizations")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# ------------------ OrgMember ------------------
class OrgMember(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="members")

    def __str__(self):
        return f"{self.name} ({self.role})"