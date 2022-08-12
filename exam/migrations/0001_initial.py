# Generated by Django 4.1 on 2022-08-12 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_day', models.DateField(blank=True, null=True)),
                ('time_from', models.TimeField(blank=True, null=True)),
                ('score_max', models.IntegerField(default=100)),
                ('required_score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Exams_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(blank=True, max_length=50)),
                ('info', models.TextField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Marking_system',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark_name', models.CharField(max_length=10)),
                ('mark_from', models.IntegerField(blank=True, null=True)),
                ('mark_until', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exam.exams')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='education.student')),
            ],
        ),
        migrations.AddField(
            model_name='exams',
            name='exam',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='exam.exams_list'),
        ),
        migrations.AddField(
            model_name='exams',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.group'),
        ),
        migrations.AddField(
            model_name='exams',
            name='room_num',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='education.room'),
        ),
    ]
