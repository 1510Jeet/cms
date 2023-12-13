from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html


# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message From (' + self.name + ')-' + self.email


class btech(models.Model):
    u_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='+')
    marksheet = models.CharField(max_length=240)
    jee = models.CharField(max_length=240)
    aadhar = models.CharField(max_length=240)
    name = models.CharField(max_length=240)
    img = models.CharField(max_length=240)
    email = models.CharField(max_length=240)
    mobile = models.BigIntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=1)
    sign = models.CharField(max_length=240)
    percent = models.DecimalField(max_digits=6, decimal_places=3)
    percentile = models.DecimalField(max_digits=6, decimal_places=3)
    category = models.CharField(max_length=240)
    certificate = models.CharField(max_length=240)
    valid = models.CharField(max_length=1)
    pincode = models.IntegerField()

    def Photo(self):
        return format_html("<a href='%s'>Photo</a>" % (self.img))

    def JEE(self):
        return format_html("<a href='%s'>JEE</a>" % (self.jee))

    def SIGN(self):
        return format_html("<a href='%s'>Sign</a>" % (self.sign))

    def Marksheet(self):
        return format_html("<a href='%s'>Marksheet</a>" % (self.marksheet))

    def Category_Certificate(self):
        return format_html("<a href='%s'>Category Certi.</a>" % (self.certificate))


class mtechcs(models.Model):
    u_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='+')
    marksheet = models.CharField(max_length=240)
    gate = models.CharField(max_length=240)
    aadhar = models.CharField(max_length=240)
    name = models.CharField(max_length=240)
    img = models.CharField(max_length=240)
    email = models.CharField(max_length=240)
    mobile = models.BigIntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=1)
    sign = models.CharField(max_length=240)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    gatescore = models.IntegerField()
    category = models.CharField(max_length=240)
    certificate = models.CharField(max_length=240)
    valid = models.CharField(max_length=1)
    pincode = models.IntegerField()

    def Photo(self):
        return format_html("<a href='%s'>Photo</a>" % (self.img))

    def GATE(self):
        return format_html("<a href='%s'>GATE</a>" % (self.gate))

    def SIGN(self):
        return format_html("<a href='%s'>Sign</a>" % (self.sign))

    def Marksheet(self):
        return format_html("<a href='%s'>Marksheet</a>" % (self.marksheet))

    def Category_Certificate(self):
        return format_html("<a href='%s'>Category Certi.</a>" % (self.certificate))


class mtechai(models.Model):
    u_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='+')
    marksheet = models.CharField(max_length=240)
    gate = models.CharField(max_length=240)
    aadhar = models.CharField(max_length=240)
    name = models.CharField(max_length=240)
    img = models.CharField(max_length=240)
    email = models.CharField(max_length=240)
    mobile = models.BigIntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=1)
    sign = models.CharField(max_length=240)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    gatescore = models.IntegerField()
    category = models.CharField(max_length=240)
    certificate = models.CharField(max_length=240)
    valid = models.CharField(max_length=1)
    pincode = models.IntegerField()

    def Photo(self):
        return format_html("<a href='%s'>Photo</a>" % (self.img))

    def GATE(self):
        return format_html("<a href='%s'>GATE</a>" % (self.gate))

    def SIGN(self):
        return format_html("<a href='%s'>Sign</a>" % (self.sign))

    def Marksheet(self):
        return format_html("<a href='%s'>Marksheet</a>" % (self.marksheet))

    def Category_Certificate(self):
        return format_html("<a href='%s'>Category Certi.</a>" % (self.certificate))


class mscdf(models.Model):
    u_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='+')
    marksheet = models.CharField(max_length=240)
    aadhar = models.CharField(max_length=240)
    name = models.CharField(max_length=240)
    img = models.CharField(max_length=240)
    email = models.CharField(max_length=240)
    mobile = models.BigIntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=1)
    sign = models.CharField(max_length=240)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    category = models.CharField(max_length=240)
    certificate = models.CharField(max_length=240)
    valid = models.CharField(max_length=1)
    pincode = models.IntegerField()

    def Photo(self):
        return format_html("<a href='%s'>Photo</a>" % (self.img))

    def SIGN(self):
        return format_html("<a href='%s'>Sign</a>" % (self.sign))

    def Marksheet(self):
        return format_html("<a href='%s'>Marksheet</a>" % (self.marksheet))

    def Category_Certificate(self):
        return format_html("<a href='%s'>Category Certi.</a>" % (self.certificate))


class pgd(models.Model):
    u_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='+')
    marksheet = models.CharField(max_length=240)
    aadhar = models.CharField(max_length=240)
    name = models.CharField(max_length=240)
    img = models.CharField(max_length=240)
    email = models.CharField(max_length=240)
    mobile = models.BigIntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=1)
    sign = models.CharField(max_length=240)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    category = models.CharField(max_length=240)
    certificate = models.CharField(max_length=240)
    valid = models.CharField(max_length=1)
    pincode = models.IntegerField()

    def Photo(self):
        return format_html("<a href='%s'>Photo</a>" % (self.img))

    def SIGN(self):
        return format_html("<a href='%s'>Sign</a>" % (self.sign))

    def Marksheet(self):
        return format_html("<a href='%s'>Marksheet</a>" % (self.marksheet))

    def Category_Certificate(self):
        return format_html("<a href='%s'>Category Certi.</a>" % (self.certificate))
