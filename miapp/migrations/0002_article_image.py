# Generated by Django 3.0.5 on 2023-04-18 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='null', upload_to=''),
        ),
    ]
