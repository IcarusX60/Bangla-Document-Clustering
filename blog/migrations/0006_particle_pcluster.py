# Generated by Django 3.2.4 on 2021-07-01 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210630_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pcluster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cluster_no', models.IntegerField(default=0)),
                ('item_count', models.IntegerField(default=0)),
                ('total_unit', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Particle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=2000, null=True)),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.pcluster')),
            ],
        ),
    ]