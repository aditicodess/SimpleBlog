# Generated by Django 4.2.3 on 2023-07-14 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='post_by_user', related_query_name='post_by_user', to=settings.AUTH_USER_MODEL, verbose_name='By User'),
        ),
    ]
