# Generated by Django 4.1.3 on 2022-12-11 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_demo2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demo',
            name='pwd',
        ),
        migrations.RemoveField(
            model_name='demo',
            name='unm',
        ),
        migrations.AddField(
            model_name='demo',
            name='city',
            field=models.TextField(default='miraj'),
        ),
        migrations.AddField(
            model_name='demo',
            name='mob',
            field=models.IntegerField(default='8999155937'),
        ),
        migrations.AddField(
            model_name='demo',
            name='nm',
            field=models.TextField(default='sabir'),
        ),
    ]