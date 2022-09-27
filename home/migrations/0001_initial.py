# Generated by Django 4.1.1 on 2022-09-27 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('technologies', models.CharField(max_length=500)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('display_picture', models.FileField(upload_to='')),
            ],
        ),
    ]
