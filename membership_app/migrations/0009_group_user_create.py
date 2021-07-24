# Generated by Django 3.2.3 on 2021-07-24 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('membership_app', '0008_auto_20210724_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='user_create',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='users_create', to='membership_app.user'),
            preserve_default=False,
        ),
    ]