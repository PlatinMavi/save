# Generated by Django 4.0.6 on 2022-10-12 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='publishdate',
            new_name='pub_date',
        ),
    ]