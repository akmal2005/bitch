# Generated by Django 4.1.3 on 2023-02-04 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sayt', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='ism_familya',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employees',
            name='lavozimi',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employees',
            name='salary',
            field=models.IntegerField(default=0, max_length=128),
            preserve_default=False,
        ),
    ]
