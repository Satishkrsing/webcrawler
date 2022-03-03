# Generated by Django 3.2.7 on 2021-10-02 09:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webcrawler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url_home',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=125),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='url_home',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Url_Monitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_monitor', models.CharField(max_length=500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=125)),
                ('url_home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webcrawler.url_home')),
            ],
        ),
    ]