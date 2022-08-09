# Generated by Django 4.1 on 2022-08-09 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('question_detail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1500)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_detail.question')),
            ],
        ),
    ]
