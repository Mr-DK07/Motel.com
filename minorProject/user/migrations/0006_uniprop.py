# Generated by Django 3.2.4 on 2023-10-10 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_nexttrip'),
    ]

    operations = [
        migrations.CreateModel(
            name='uniprop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uppic', models.ImageField(null=True, upload_to='static/upropic')),
                ('upname', models.CharField(max_length=200, null=True)),
                ('uplocation', models.CharField(max_length=500, null=True)),
                ('uprating', models.FloatField(max_length=20, null=True)),
                ('upreviews', models.CharField(max_length=200, null=True)),
                ('update', models.DateField()),
            ],
        ),
    ]