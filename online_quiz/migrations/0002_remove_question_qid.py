# Generated by Django 3.1.1 on 2020-09-04 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='qid',
        ),
    ]
