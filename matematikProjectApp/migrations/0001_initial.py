# Generated by Django 3.1.7 on 2021-04-10 16:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Not',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslık', models.CharField(max_length=75, verbose_name='Başlık')),
                ('noticerik', ckeditor.fields.RichTextField(blank=True, verbose_name='Notunuz')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Notlar',
            },
        ),
    ]
