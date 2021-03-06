# Generated by Django 3.2.3 on 2021-07-24 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('membership_app', '0003_auto_20210724_1005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='members',
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(related_name='groups_2', to='membership_app.User'),
        ),
        migrations.AlterField(
            model_name='group',
            name='user_create',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='membership_app.user'),
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
