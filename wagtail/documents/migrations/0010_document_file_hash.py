# Generated by Django 2.1.2 on 2018-10-28 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0009_document_verbose_name_plural'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='file_hash',
            field=models.CharField(null=True, blank=True, editable=False, max_length=40),
        ),
    ]
