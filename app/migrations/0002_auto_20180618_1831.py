# Generated by Django 2.0.6 on 2018-06-18 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='title',
            field=models.CharField(default='title', max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='uservote',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
