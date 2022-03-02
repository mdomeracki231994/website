from django.db import models


class Services(models.Model):
    service_name = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=255, null=True)
    icon_html = models.CharField(max_length=255, null=True)


class UserInfo(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=255, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    message = models.TextField()


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='employee_images/')
    facebook_link = models.CharField(max_length=100)
    linkedin_link = models.CharField(max_length=100)
    twitter_link = models.CharField(max_length=100)

    # TODO Figure out why I cannot delete.
    # def __str__(self):
    #     return self.first_name, self.last_name


class Portfolio(models.Model):
    company_name = models.CharField(max_length=255)
    company_description = models.TextField(null=True)
    services_provided = models.CharField(max_length=255)
    company_long_description = models.TextField(null=True)
    company_image = models.ImageField(upload_to='company_images/', null=True, blank=True)


