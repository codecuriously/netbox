# Generated by Django 5.0.6 on 2024-06-04 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualization', '0039_convert_disk_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='virtualmachine',
            name='serial',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
