# Generated by Django 4.0.2 on 2022-03-01 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_employee_alter_userinfo_email_alter_userinfo_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_image',
            field=models.ImageField(upload_to='employee_images/'),
        ),
    ]
