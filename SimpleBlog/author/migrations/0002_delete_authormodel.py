# Generated by Django 4.2.3 on 2023-07-14 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_postmodel_author'),
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthorModel',
        ),
    ]
