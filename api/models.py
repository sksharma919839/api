from django.db import models


class about(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to="image/")
    upload_to = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class projectHome(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="image/")
    h = models.CharField(max_length=255)
    p = models.CharField(max_length=999)
    link = models.CharField(max_length=999)

    def __str__(self):
        return self.h


class project(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="image/")
    h = models.CharField(max_length=255)
    p = models.CharField(max_length=999)
    link = models.CharField(max_length=999)

    def __str__(self):
        return self.h


class cv(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    pdf = models.FileField(upload_to="pdf/")
    upload_to = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class contact(models.Model):
    name = models.CharField(max_length=355)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=10)
    message = models.CharField(max_length=999)
