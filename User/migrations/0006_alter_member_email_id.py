# Generated by Django 4.1 on 2022-12-09 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_department_role_remove_member_dept_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email_id',
            field=models.EmailField(max_length=254),
        ),
    ]
