# Generated by Django 3.1.7 on 2021-03-19 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_article_theme'),
    ]

    operations = [
        migrations.RenameField(
            model_name='decor',
            old_name='Material',
            new_name='material',
        ),
        migrations.RenameField(
            model_name='decor',
            old_name='Price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='decor',
            old_name='Quantity',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='dishes',
            old_name='Type',
            new_name='kind',
        ),
        migrations.RenameField(
            model_name='dishes',
            old_name='Material',
            new_name='material',
        ),
        migrations.RenameField(
            model_name='dishes',
            old_name='Price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='dishes',
            old_name='Quantity',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='pot',
            old_name='Material',
            new_name='material',
        ),
        migrations.RenameField(
            model_name='pot',
            old_name='Price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='pot',
            old_name='Quantity',
            new_name='quantity',
        ),
        migrations.RemoveField(
            model_name='decor',
            name='Style',
        ),
        migrations.RemoveField(
            model_name='dishes',
            name='Style',
        ),
        migrations.RemoveField(
            model_name='pot',
            name='Style',
        ),
        migrations.AddField(
            model_name='decor',
            name='style',
            field=models.ManyToManyField(help_text='Стиль', to='catalog.style'),
        ),
        migrations.AddField(
            model_name='dishes',
            name='style',
            field=models.ManyToManyField(help_text='Стиль', to='catalog.style'),
        ),
        migrations.AddField(
            model_name='pot',
            name='style',
            field=models.ManyToManyField(help_text='Стиль', to='catalog.style'),
        ),
    ]
