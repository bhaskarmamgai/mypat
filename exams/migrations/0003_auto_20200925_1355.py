# Generated by Django 3.1.1 on 2020-09-25 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_auto_20200925_1351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='sub_category',
            new_name='exams',
        ),
        migrations.AlterField(
            model_name='exams',
            name='code',
            field=models.CharField(max_length=20, unique=True, verbose_name='Examination Code'),
        ),
    ]
