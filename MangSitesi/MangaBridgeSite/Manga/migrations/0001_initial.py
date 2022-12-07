# Generated by Django 4.0.6 on 2022-10-20 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('Number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MangaName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Translators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Translator', models.CharField(max_length=30)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manga.chapter')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='manga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manga.manga'),
        ),
    ]