# Generated by Django 3.2.3 on 2021-05-27 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('categoria', models.CharField(max_length=30)),
                ('autor', models.CharField(max_length=30)),
            ],
        ),
    ]