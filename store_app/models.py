from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255)
    wikipedia_link = models.URLField()

class Course(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)
    mail_id = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=255)
    materials_provided = models.CharField(max_length=255)

    def __str__(self):
        return self.name
