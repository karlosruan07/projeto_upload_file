# Generated by Django 3.1.3 on 2020-12-19 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_upload_file', '0004_uploadfiles_data_criacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publi_date', models.DateField()),
                ('headline', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_upload_file.reporter')),
            ],
        ),
    ]