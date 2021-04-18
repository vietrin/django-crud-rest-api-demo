# Generated by Django 3.1.7 on 2021-04-18 15:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.UUIDField(default=uuid.UUID('31e2cd65-db1a-4472-95f6-f98ba17c3996'), editable=False, primary_key=True, serialize=False),
        ),
    ]