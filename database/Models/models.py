# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    admin_name = models.CharField(db_column='Admin_name', max_length=10)  # Field name made lowercase.
    admin_id = models.CharField(db_column='Admin_id', primary_key=True, max_length=20)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Admin'


class Donate(models.Model):
    donate_id = models.CharField(db_column='Donate_id', primary_key=True, max_length=20)  # Field name made lowercase.
    donor = models.ForeignKey('Donor', models.DO_NOTHING, db_column='Donor_id')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    project = models.ForeignKey('Project', models.DO_NOTHING, db_column='Project_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Donate'


class Donor(models.Model):
    donor_name = models.CharField(db_column='Donor_name', max_length=10)  # Field name made lowercase.
    donor_id = models.CharField(db_column='Donor_id', primary_key=True, max_length=20)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Donor'


class Fund(models.Model):
    fund_id = models.CharField(db_column='Fund_id', max_length=20)  # Field name made lowercase.
    project_id = models.CharField(db_column='Project_id', primary_key=True, max_length=40)  # Field name made lowercase.
    donor_num = models.IntegerField(db_column='Donor_num')  # Field name made lowercase.
    cum_amount = models.DecimalField(db_column='Cum_amount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    target_amount = models.DecimalField(db_column='Target_amount', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fund'
        unique_together = (('project_id', 'fund_id'),)


class Initiate(models.Model):
    ini_name = models.ForeignKey('Initiator', models.DO_NOTHING, db_column='Ini_name')  # Field name made lowercase.
    project = models.OneToOneField('Project', models.DO_NOTHING, db_column='Project_id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Initiate'


class Initiator(models.Model):
    ini_name = models.CharField(db_column='Ini_name', primary_key=True, max_length=30)  # Field name made lowercase.
    ini_contact = models.CharField(db_column='Ini_contact', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Initiator'


class Manage(models.Model):
    admin = models.ForeignKey(Admin, models.DO_NOTHING, db_column='Admin_id')  # Field name made lowercase.
    project = models.ForeignKey('Project', models.DO_NOTHING, db_column='Project_id')  # Field name made lowercase.
    manage_id = models.CharField(db_column='Manage_id', primary_key=True, max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Manage'


class Project(models.Model):
    project_name = models.CharField(db_column='Project_name', max_length=20)  # Field name made lowercase.
    project_id = models.CharField(db_column='Project_id', primary_key=True, max_length=40)  # Field name made lowercase.
    duration = models.CharField(db_column='Duration', max_length=30)  # Field name made lowercase.
    start_date = models.DateField(db_column='Start_date')  # Field name made lowercase.
    end_date = models.DateField(db_column='End_date', blank=True, null=True)  # Field name made lowercase.
    introduction = models.CharField(db_column='Introduction', max_length=60)  # Field name made lowercase.
    project_province = models.CharField(db_column='Project_province', max_length=10)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=10)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Project'


class Receive(models.Model):
    reci_name = models.ForeignKey('Recipient', models.DO_NOTHING, db_column='Reci_name')  # Field name made lowercase.
    project = models.OneToOneField(Project, models.DO_NOTHING, db_column='Project_id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Receive'


class Recipient(models.Model):
    reci_name = models.CharField(db_column='Reci_name', primary_key=True, max_length=30)  # Field name made lowercase.
    reci_contact = models.CharField(db_column='Reci_contact', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Recipient'


# class User(models.Model):
#     user_name = models.CharField(db_column='User_name', max_length=30)  # Field name made lowercase.
#     user_id = models.CharField(db_column='User_id', primary_key=True, max_length=30)  # Field name made lowercase.
#     password = models.CharField(db_column='Password', max_length=30)  # Field name made lowercase.
#     role = models.CharField(db_column='Role', max_length=10)  # Field name made lowercase.
# 
#     class Meta:
#         managed = False
#         db_table = 'User'
