# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    role = models.CharField(max_length=255, null=True, blank=True)
    permisions = models.CharField(max_length=255, null=True, blank=True)
    profilepicture = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Customers(models.Model):

    #__Customers_FIELDS__
    customer = models.TextField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=255, null=True, blank=True)
    officenumber = models.CharField(max_length=255, null=True, blank=True)
    company = models.TextField(max_length=255, null=True, blank=True)
    rep = models.TextField(max_length=255, null=True, blank=True)
    dateadded = models.DateTimeField(blank=True, null=True, default=timezone.now)
    lastvisiteddate = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Customers_FIELDS__END

    class Meta:
        verbose_name        = _("Customers")
        verbose_name_plural = _("Customers")


class Quoterequest(models.Model):

    #__Quoterequest_FIELDS__
    description = models.TextField(max_length=255, null=True, blank=True)
    status = models.TextField(max_length=255, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    noteslink = models.TextField(max_length=255, null=True, blank=True)

    #__Quoterequest_FIELDS__END

    class Meta:
        verbose_name        = _("Quoterequest")
        verbose_name_plural = _("Quoterequest")


class Suppliers(models.Model):

    #__Suppliers_FIELDS__
    coordinates = models.TextField(max_length=255, null=True, blank=True)
    closingtime = models.TextField(max_length=255, null=True, blank=True)
    suppliername = models.TextField(max_length=255, null=True, blank=True)
    suppliernumber = models.TextField(max_length=255, null=True, blank=True)
    supplieraddress = models.TextField(max_length=255, null=True, blank=True)

    #__Suppliers_FIELDS__END

    class Meta:
        verbose_name        = _("Suppliers")
        verbose_name_plural = _("Suppliers")


class Company(models.Model):

    #__Company_FIELDS__
    company = models.TextField(max_length=255, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)

    #__Company_FIELDS__END

    class Meta:
        verbose_name        = _("Company")
        verbose_name_plural = _("Company")


class Orders(models.Model):

    #__Orders_FIELDS__
    orderdate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    company = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True)
    status = models.TextField(max_length=255, null=True, blank=True)

    #__Orders_FIELDS__END

    class Meta:
        verbose_name        = _("Orders")
        verbose_name_plural = _("Orders")


class Driverlist(models.Model):

    #__Driverlist_FIELDS__
    qty = models.IntegerField(null=True, blank=True)
    supplier = models.TextField(max_length=255, null=True, blank=True)
    status = models.TextField(max_length=255, null=True, blank=True)
    completeddate = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Driverlist_FIELDS__END

    class Meta:
        verbose_name        = _("Driverlist")
        verbose_name_plural = _("Driverlist")



#__MODELS__END
