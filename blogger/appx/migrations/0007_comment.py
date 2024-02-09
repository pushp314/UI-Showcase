# Generated by Django 5.0 on 2024-02-01 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appx', '0006_blogx_slugx'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cum', models.TextField(max_length=200, null=True)),
                ('cum_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appx.blogx')),
            ],
        ),
    ]