# Generated by Django 3.0.5 on 2020-04-30 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20200430_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(default=None, upload_to='covers/'),
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='book',
            name='is_published',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='book',
            name='published',
            field=models.DateField(default=None),
        ),
    ]
