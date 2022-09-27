# Generated by Django 3.2.2 on 2021-05-11 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=500)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
    ]