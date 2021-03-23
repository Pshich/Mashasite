# Generated by Django 3.1.7 on 2021-03-14 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='ВВедите размер', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='material',
            name='name',
            field=models.CharField(help_text='ВВедите материал', max_length=20),
        ),
    ]