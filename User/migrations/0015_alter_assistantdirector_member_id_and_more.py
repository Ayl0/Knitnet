# Generated by Django 4.0.8 on 2022-12-11 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0014_remove_sponsor_sponsor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistantdirector',
            name='member_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='director',
            name='member_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ec',
            name='member_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='patron',
            name='member_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='member_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]