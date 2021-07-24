# Generated by Django 3.2.3 on 2021-07-24 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('membership_app', '0010_rename_desription_group_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='member',
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users', models.FloatField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group', to='membership_app.group')),
            ],
        ),
    ]
