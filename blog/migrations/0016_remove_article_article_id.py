# Generated by Django 3.2.4 on 2021-07-02 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_article_article_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_id',
        ),
    ]
