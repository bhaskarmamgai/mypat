# Generated by Django 3.1.1 on 2020-09-25 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0003_auto_20200925_1355'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='exams',
            new_name='exam',
        ),
    ]
