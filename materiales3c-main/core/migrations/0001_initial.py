# Generated by Django 4.2.5 on 2023-10-27 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GrantGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gg_tittle', models.CharField(default='Generic Grant Goal Tittle', max_length=128)),
                ('description', models.CharField(default='Generic Grant Goal Description', max_length=256)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('days_duration', models.IntegerField(default=7)),
                ('final_date', models.DateField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('state', models.CharField(choices=[('Done', 'DN'), ('Doing', 'DG'), ('Not Stared', 'NS')], max_length=16)),
                ('sprint', models.IntegerField(default=1)),
                ('slug', models.SlugField(max_length=16)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
