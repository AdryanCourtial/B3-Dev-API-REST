# Generated by Django 5.1.1 on 2024-10-04 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='birthday',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='books',
            name='year_of_publication',
            field=models.TextField(),
        ),
    ]
