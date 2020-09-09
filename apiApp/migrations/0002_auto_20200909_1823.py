# Generated by Django 3.1.1 on 2020-09-09 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='description',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='title',
        ),
        migrations.AddField(
            model_name='movie',
            name='auto_reg_no',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='movie',
            name='city',
            field=models.CharField(max_length=36, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='mobile',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=36, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='movie',
            name='regular_stand',
            field=models.CharField(max_length=36, null=True),
        ),
    ]