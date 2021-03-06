# Generated by Django 3.0.6 on 2020-05-27 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chapters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('question_title', models.TextField(blank=True, null=True)),
                ('question_type', models.CharField(blank=True, max_length=100, null=True)),
                ('question_img_url', models.TextField(blank=True, null=True)),
                ('difficulty_level', models.CharField(choices=[('easy', 'Easy'), ('moderate', 'Moderate'), ('difficult', 'Difficult')], db_index=True, default='moderate', max_length=50)),
                ('time_to_solve', models.IntegerField(blank=True, null=True)),
                ('answer_selection_type', models.CharField(db_index=True, default='single_choice', max_length=50)),
                ('explanation', models.TextField(blank=True, null=True)),
                ('explanation_img_url', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.TextField()),
                ('choice_img_url', models.TextField(blank=True, null=True)),
                ('is_right_choice', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionChapterMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chapters.Chapter')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question')),
            ],
            options={
                'unique_together': {('question', 'chapter')},
            },
        ),
    ]
