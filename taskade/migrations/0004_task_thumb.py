# Generated by Django 5.0.6 on 2024-11-13 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskade', '0003_alter_task_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
