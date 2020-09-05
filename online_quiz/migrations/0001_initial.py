# Generated by Django 3.1.1 on 2020-09-04 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qid', models.IntegerField(default='', verbose_name='Question Id')),
                ('content', models.CharField(help_text='Enter the question text that you want displayed', max_length=1000, verbose_name='Question')),
                ('option1', models.TextField(blank=True, max_length=40, null=True)),
                ('option2', models.TextField(blank=True, max_length=40, null=True)),
                ('option3', models.TextField(blank=True, max_length=40, null=True)),
                ('option4', models.TextField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(blank=True, max_length=40, null=True, verbose_name='Correct Answer')),
                ('qid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_quiz.question', verbose_name='Question')),
            ],
        ),
    ]
