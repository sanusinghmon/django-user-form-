# Generated by Django 4.0.6 on 2022-07-18 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythondata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinsert',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userinsert',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userinsert',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]