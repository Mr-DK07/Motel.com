# Generated by Django 3.2.4 on 2024-06-08 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0025_rename_countaryname_userdetails_countryname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='register',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
