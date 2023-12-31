# Generated by Django 4.2.3 on 2023-07-14 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '__first__'),
        ('category', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('content', models.CharField(max_length=200)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='post/')),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='post_by_user', related_query_name='post_by_user', to='author.authormodel', verbose_name='By User')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.categorymodel')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'db_table': 'post',
                'ordering': ['-date_posted'],
            },
        ),
    ]
