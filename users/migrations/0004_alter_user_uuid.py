# Generated by Django 4.2.17 on 2025-02-06 15:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_refreshtoken_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
