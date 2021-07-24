# Generated by Django 3.2.3 on 2021-07-24 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('membership_app', '0006_delete_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desription', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('member', models.ManyToManyField(related_name='members', to='membership_app.User')),
                ('user_create', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_create', to='membership_app.user')),
            ],
        ),
    ]