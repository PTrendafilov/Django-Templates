# Generated by Django 4.0.4 on 2022-05-25 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_text', models.CharField(max_length=200)),
                ('is_finished', models.BooleanField(default=False)),
                ('deadline', models.DateField()),
            ],
        ),
    ]
