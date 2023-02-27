# Generated by Django 4.1.3 on 2023-01-23 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]
