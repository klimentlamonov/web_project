# Generated by Django 2.2.16 on 2020-09-22 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50, verbose_name='Имя')),
                ('password', models.CharField(max_length=50, verbose_name='Пароль')),
            ],
        ),
    ]
