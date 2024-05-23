# Generated by Django 4.2.5 on 2023-11-03 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InfoHaven_App', '0015_remove_member_borrowed_books_book_summary_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowingrecord',
            name='Member_ID',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='borrowingrecord',
            name='book_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='InfoHaven_App.book'),
        ),
    ]
