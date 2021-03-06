# Generated by Django 2.2.6 on 2019-11-17 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('analyzer', '0002_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewedProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=1000, unique=True)),
                ('p_url', models.CharField(max_length=1000, unique=True)),
                ('r_count', models.IntegerField()),
                ('p_rating', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_star', models.CharField(max_length=1)),
                ('r_title', models.TextField()),
                ('r_body', models.TextField()),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analyzer.ViewedProducts')),
            ],
        ),
    ]
