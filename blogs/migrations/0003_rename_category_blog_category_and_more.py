# Generated by Django 4.1.7 on 2023-07-16 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_category_options_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='Category_name',
            new_name='category_name',
        ),
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Publish', 'Publish')], default='Draft', max_length=20),
        ),
    ]
