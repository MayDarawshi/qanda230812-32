# Generated by Django 4.1 on 2022-08-22 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_questions_q_image_alter_teachers_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='q_image',
        ),
        migrations.AddField(
            model_name='questions',
            name='title',
            field=models.CharField(default='may', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='questions',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.teachers'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.CharField(max_length=1000),
        ),
        migrations.CreateModel(
            name='reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('dis', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.teachers')),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.CharField(max_length=7)),
                ('text_answer', models.CharField(max_length=500)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.questions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.users')),
            ],
        ),
    ]
