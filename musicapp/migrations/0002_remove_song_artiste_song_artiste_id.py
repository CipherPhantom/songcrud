# Generated by Django 4.1.2 on 2022-10-28 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='Artiste',
        ),
        migrations.AddField(
            model_name='song',
            name='artiste_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='musicapp.artiste'),
            preserve_default=False,
        ),
    ]
