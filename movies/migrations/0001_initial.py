# Generated by Django 3.1 on 2020-08-28 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('rating', models.CharField(blank=True, default='', max_length=2)),
                ('imdb_key', models.CharField(blank=True, default='', max_length=15)),
                ('type_rating', models.CharField(blank=True, default='', max_length=5)),
                ('duration', models.CharField(blank=True, default='', max_length=20)),
                ('genre', models.CharField(blank=True, default='', max_length=50)),
                ('release_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched', models.BooleanField(default=False)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]