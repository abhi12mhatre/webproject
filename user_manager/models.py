from django.contrib.auth.models import User
from django.db import models

from constants.Constants import RecordStatus, Gender


class Record(models.Model):
    status = models.PositiveSmallIntegerField(default=RecordStatus.ACTIVE, choices=RecordStatus.CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(models.Model):
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    gender = models.PositiveSmallIntegerField(choices=Gender.CHOICES, default=Gender.MALE)
    dob = models.DateField()
    email = models.EmailField(null=True, blank=True)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    alternate_phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return '{} {} {}'.format(self.firstname, self.middlename or '', self.lastname or '')

    class Meta:
        abstract = True


class UserProfile(Profile, Record):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class UserExtra(Record):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    value = models.TextField()

    def __str__(self):
        return self.label


class Experience(Record):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)
    company_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)


class Resume(Record):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    user_extra = models.ManyToManyField(UserExtra)
    experience = models.ManyToManyField(Experience)
    objective = models.TextField(null=True, blank=True)
