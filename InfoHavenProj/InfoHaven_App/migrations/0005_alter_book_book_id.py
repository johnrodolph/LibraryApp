# Generated by Django 4.2.5 on 2023-10-09 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfoHaven_App', '0004_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
