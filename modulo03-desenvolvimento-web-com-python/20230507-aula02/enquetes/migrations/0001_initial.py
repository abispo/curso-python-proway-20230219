# Generated by Django 4.2 on 2023-04-30 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=200)),
                ('data_de_publicacao', models.DateTimeField(verbose_name='Data de publicação')),
            ],
        ),
    ]
