# Generated by Django 4.1.1 on 2022-09-29 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('compile', models.BooleanField(default=False)),
            ],
        ),
    ]
