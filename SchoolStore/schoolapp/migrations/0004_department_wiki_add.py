# Generated by Django 4.1.4 on 2023-04-10 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0003_remove_department_courses_alter_course_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='wiki_add',
            field=models.TextField(blank=True),
        ),
    ]
