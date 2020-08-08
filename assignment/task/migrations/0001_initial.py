# Generated by Django 3.0.4 on 2020-08-08 06:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.CharField(blank=True, default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('task_type', models.IntegerField(choices=[(1, 'Type_1'), (2, 'Type_2'), (3, 'Type_3'), (4, 'Type_4')])),
                ('task_desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TaskTracker',
            fields=[
                ('task_typeTracker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='task_typeTracker', serialize=False, to='task.Task')),
                ('update_type', models.IntegerField(choices=[(1, 'per_Day'), (7, 'per_Week'), (30, 'per_Monthly')])),
                ('email', models.EmailField(blank=True, max_length=100)),
            ],
        ),
    ]