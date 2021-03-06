# Generated by Django 3.1.1 on 2022-06-05 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SnsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('author', models.CharField(max_length=50)),
                ('sns_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('good', models.IntegerField(null=True)),
                ('read', models.IntegerField(null=True)),
                ('readText', models.TextField(blank=True)),
            ],
        ),
    ]
