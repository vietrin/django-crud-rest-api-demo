# Generated by Django 3.1.7 on 2021-04-18 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.UUIDField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=250)),
            ],
        ),
    ]