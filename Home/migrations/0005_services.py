# Generated by Django 4.0.2 on 2022-03-02 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('icon_html', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
