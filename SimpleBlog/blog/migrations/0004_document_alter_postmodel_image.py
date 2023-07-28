# Generated by Django 4.2.3 on 2023-07-15 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_postmodel_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(upload_to='media/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]