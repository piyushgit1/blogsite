# Generated by Django 3.0.2 on 2020-04-18 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0016_auto_20200418_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(default='Write here'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default='title', max_length=250),
        ),
    ]