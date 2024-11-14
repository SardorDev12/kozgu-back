# Generated by Django 5.1.3 on 2024-11-14 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_name'),
        ('posts', '0005_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='posts', to='categories.category'),
        ),
    ]
