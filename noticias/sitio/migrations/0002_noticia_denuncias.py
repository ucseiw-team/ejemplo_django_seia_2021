# Generated by Django 3.2.6 on 2021-08-11 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='denuncias',
            field=models.IntegerField(default=0),
        ),
    ]