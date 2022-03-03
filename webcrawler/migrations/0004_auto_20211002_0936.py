# Generated by Django 3.2.7 on 2021-10-02 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcrawler', '0003_auto_20211002_0908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Url_blacklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_blacklist', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='url_monitor',
            name='name',
        ),
        migrations.AddField(
            model_name='url_home',
            name='blacklist',
            field=models.BooleanField(default=False),
        ),
    ]